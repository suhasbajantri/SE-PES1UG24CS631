

\# Lab 5: Static Code Analysis — Issues



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| SQL injection risk | Security | Check report | SQL query constructed using an f-string | Use parameterized SQL placeholders |

| Shell command execution | Security | Check report | Command executed with shell=True | Replace shell execution with a safe dispatch message |

| Unsafe file handling | Code quality | Check report | File opened without guaranteed closure | Use a with statement and specify encoding |

| Broad exception handling | Bug / Code quality | Check report | Bare except hides unrelated errors | Remove unnecessary exception handling and handle the actual result |

| Naming and style violations | Style | Check report | Function names and formatting are inconsistent | Use snake\_case and consistent formatting |



\## Verification



\- Ran Pylint before and after changes.

\- Ran Bandit before and after changes.

\- Ran Flake8 before and after changes.

\- Tested the school transport demonstration after editing.



