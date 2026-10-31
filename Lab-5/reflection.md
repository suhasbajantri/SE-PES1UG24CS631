

\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis?



Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, maintainability problems, and style violations.



\## 2. What did Pylint, Bandit, and Flake8 help identify?



Pylint helped assess code quality, naming, and programming practices. Bandit helped identify potentially insecure coding patterns. Flake8 helped detect formatting and style violations.



\## 3. What issues did you fix?



I replaced dynamically constructed SQL with parameterized queries, removed shell-based command execution, improved file handling with a context manager, and simplified fee calculation by removing unnecessary broad exception handling.



\## 4. Why is static analysis useful?



Static analysis helps developers identify problems earlier, improve security and readability, and maintain consistent coding standards. Running the tools again after making changes helps verify that reported issues have been addressed.



