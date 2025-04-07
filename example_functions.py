import time
from profiler import profiler

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
    Simulates a slow task (1s)
    """
    time.sleep(1)

# Enable profiling for specific functions
profiler.enable(functions={"fast_function", "medium_function", "slow_function"})

# Call the functions using the context manager
def run_example():
    with profiler.profile("fast_function"):
        fast_function()
    with profiler.profile("medium_function"):
        medium_function()
    with profiler.profile("slow_function"):
        slow_function()

# Run the example
if __name__ == "__main__":
    run_example()
    # Disable profiling and print results
    profiler.disable()
    profiler.print_results()