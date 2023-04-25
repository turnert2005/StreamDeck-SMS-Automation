---

# Testing Instructions

This document outlines the process of running unit tests for the Stream Deck SMS project.

## Prerequisites

Before running the tests, ensure you have Python installed on your system. The `unittest` framework is pre-installed with Python, so you typically won't need to do anything. If you are using an older version of Python, you might need to install it using `pip install unittest2`.

## Test Files

The following test files should be present in your project directory:

- `test_config.py`
- `test_sms_server.py`
- `test_send_sms_trigger.py`

These test files correspond to the Python modules:

- `config.py`
- `sms_server.py`
- `send_sms_trigger.py`

Additionally, there is a new file named `dependencies.py` that checks and installs required packages.

## Running Tests

To run the tests, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory where the test files and Python modules are located.

3. Before running the tests, ensure you have installed the required packages by running:

   ```
   python dependencies.py
   ```

4. Run all test files by executing the following command:

   ```
   python -m unittest discover
   ```

   This command will discover and run all the test files in your project directory that match the pattern `test*.py`.

5. Alternatively, you can run individual test files by executing the command:

   ```
   python test_sms_server.py
   ```

   Make sure to replace `test_sms_server.py` with the name of the test file you want to run.

6. After running the tests, you will see the results in your terminal or command prompt, which will show you how many tests have passed and if any have failed.

7. If any tests fail, you should examine the error messages and modify your code accordingly to fix the issues.

## Benefits of Testing

Regularly running unit tests as you develop your application helps you catch bugs early, ensures your code works as expected, and makes it easier to maintain and refactor your code.