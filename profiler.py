import sys
import time
import json
from tabulate import tabulate

class SysProfiler:
    def __init__(self, config_file):
        self.results = {}
        self.functions_to_trace = set()
        self.load_config(config_file)
        self.current_function = None
        self.start_time = None

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
        self.functions_to_trace = set(config["functions_to_profile"])

    def profile_function(self, frame, event, arg):
        if event == 'call':
            func_name = frame.f_code.co_name
            if func_name in self.functions_to_trace:
                self.current_function = func_name
                self.start_time = time.time()
        elif event == 'return' and self.current_function:
            elapsed_time = time.time() - self.start_time
            if self.current_function not in self.results:
                self.results[self.current_function] = []
            self.results[self.current_function].append(elapsed_time)
            self.current_function = None

    def enable(self):
        sys.setprofile(self.profile_function)

    def disable(self):
        sys.setprofile(None)

    def disable_function(self, func_name):
        """Dynamically disable profiling for a specific function."""
        if func_name in self.functions_to_trace:
            self.functions_to_trace.remove(func_name)

    def print_results(self):
        print("Profiling Results:")
        table = []
        for func_name, times in self.results.items():
            average_time = sum(times) / len(times)
            table.append([func_name, f"{average_time:.6f}", len(times)])
        headers = ["Function Name", "Average Time (s)", "Number of Runs"]
        print(tabulate(table, headers=headers, tablefmt="grid"))