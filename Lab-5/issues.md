\# Lab 5: Static Code Analysis — Issues



\## Issues Identified and Fixed



| Issue | Tool | Type | Description | Fix Applied |

|---|---|---|---|---|

| SQL injection risk (B608) | Bandit | Security | SQL query was constructed using an f-string with user data. | Replaced string construction with parameterized SQL using `?` placeholders. |

| Shell command execution (B602) | Bandit | High Security | `subprocess.run()` was used with `shell=True`, creating a command injection risk. | Removed shell-based execution and replaced it with a safe Python dispatch message. |

| Use of assert (B101) | Bandit | Security / Reliability | `assert` was used for runtime validation and may be removed in optimized execution. | Replaced the assertion with an explicit `if` check that raises `ValueError`. |

| Unsafe subprocess import (B404) | Bandit | Security | The `subprocess` module was imported and used in insecure command execution. | Removed the unnecessary `subprocess` import and shell command usage. |

| Unsafe file handling | Pylint | Code Quality | File handling did not guarantee closure and did not specify an encoding. | Used `with open(..., encoding="utf-8")` for safe resource handling. |

| Bare exception (W0702 / E722) | Pylint / Flake8 | Code Quality | A bare `except` could hide unexpected errors. | Removed the broad exception handling and used explicit validation. |

| Naming and formatting violations | Pylint / Flake8 | Style | Function names, spacing, line lengths, blank lines, and documentation did not follow standards. | Applied snake\_case naming, proper spacing, line formatting, and docstrings. |



\## Verification Results



\### Before Fixes



\- \*\*Pylint:\*\* 4.00/10

\- \*\*Bandit:\*\* 4 issues identified, including one High severity issue.

\- \*\*Flake8:\*\* Multiple formatting and style violations were reported.



\### After Fixes



\- \*\*Pylint:\*\* 10.00/10

\- \*\*Bandit:\*\* No issues identified.

\- \*\*Flake8:\*\* No output, indicating no remaining violations.



All three static analysis tools were run again after the fixes to verify the final results.

