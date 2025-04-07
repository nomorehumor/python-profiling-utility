# Python Function Profiler

This project provides a utility for profiling the execution time of specific functions in a Python program using `sys.setprofile()`. It allows you to dynamically enable and disable profiling for specified functions without modifying their definitions.

The `sys.setprofile()` is used, since it allows us tracing without modifications of target functions and works on more python versions than sys.monitoring, although presents small overhead.

## Features
- Profile specific functions without modifying them directly.
- Dynamically enable or disable profiling for specific functions.
- Display profiling results in a clear table format.
- Specify functions to profile using a JSON configuration file.
- Use command-line arguments to specify the configuration file.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**
   Make sure you have Python installed. You can install the required Python package using pip:
   ```bash
   pip install -r requirements.txt 
   ```

## Usage

1. **Create a Configuration File**
   Create a JSON configuration file (e.g., `config.json`) to specify which functions to profile:
   ```json
   {
       "functions_to_profile": [
           "fast_function",
           "medium_function",
           "slow_function"
       ]
   }
   ```

2. **Run the example profiler script**
   Use the command-line to run the profiler with the specified configuration file:
   ```bash
   python execute_profiler.py --config config.json
   ```
   You can specify a different configuration file if needed.

## Example

The `example_functions.py` script demonstrates how to use the profiler. It includes three functions (`fast_function`, `medium_function`, `slow_function`) that simulate tasks of varying durations.

## License

This project is licensed under the MIT License. See the LICENSE file for more details. 