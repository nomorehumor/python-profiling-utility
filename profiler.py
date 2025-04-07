import time
from contextlib import contextmanager

class Profiler:
    def __init__(self):
        self.enabled = False
        self.results = {}
        self.functions_to_trace = set()

    def enable(self, functions=None):
        self.enabled = True
        if functions:
            self.functions_to_trace.update(functions)

    def disable(self):
        self.enabled = False

    def get_results(self):
        return self.results

    @contextmanager
    def profile(self, func_name):
        if self.enabled and func_name in self.functions_to_trace:
            start_time = time.time()
            yield
            end_time = time.time()
            elapsed_time = end_time - start_time
            if func_name not in self.results:
                self.results[func_name] = []
            self.results[func_name].append(elapsed_time)
        else:
            yield

    def print_results(self):
        print("Profiling Results:")
        for func_name, times in self.results.items():
            print(f"{func_name}: {sum(times)/len(times):.6f} seconds (average over {len(times)} runs)")

# Create a global profiler instance
profiler = Profiler() 