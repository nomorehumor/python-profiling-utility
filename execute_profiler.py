import argparse
import time
from profiler import SysProfiler

def fast_function():
    """
    Simulates a fast task (0.05s)
    """
    time.sleep(0.05)

def medium_function():
    """
    Simulates a medium-duration task (0.1s)
    """
    time.sleep(0.1)

def slow_function():
    """
    Simulates a slow task (0.2s)
    """
    time.sleep(0.2)

if __name__ == "__main__":
    # Initialize the profiler with the configuration file
    parser = argparse.ArgumentParser(description='Run functions with profiling.')
    parser.add_argument('--config', type=str, default='config.json', help='Path to the configuration file')
    args = parser.parse_args()

    # Initialize the profiler with the configuration file
    profiler = SysProfiler(args.config)     
    profiler.enable()

    # Call the functions
    for i in range(20):
        fast_function()
        medium_function()
        slow_function()
        if i == 10:
            profiler.disable_function("fast_function")
            print("====Intermediate results====")
            profiler.print_results()

    # Disable profiling and print results
    print("====Final results====")

    profiler.disable()
    profiler.print_results()