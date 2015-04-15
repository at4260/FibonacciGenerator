# Fibonacci Generator
App that generates the nth value in the Fibonacci sequence

- Controller.py - incorporates gevent library to host Flask server on port 8000 instead of port 5000
- Utils.py - Fibonacci function written recursively
  - Optimized multiple server request by using memoization and creating a decorator
- Unit_tests.py and Integration_tests.py - created tests to check result of Fibonacci function
