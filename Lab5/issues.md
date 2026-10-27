# Identified issues and fixes

Shreya Yashodhara Singh | PES1UG24AM266

Line numbers refer to original/address_book.py. Bandit severity labels are tool-reported; other rows are not assigned invented severity levels.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| B324 / High | Security | 19 | MD5 used for contact ID. | Use SHA-256; retain six hexadecimal display characters. Not an authentication token. |
| B301 / Medium | Security | 65-67 | pickle.load can execute code from a malicious backup. | Use json.load/json.dump with UTF-8 text files. Regenerate old pickle backups. |
| B403 / Low | Security | 3 | Import of pickle introduces an unsafe serialization facility. | Remove pickle and import json. |
| B105 / Low | Security | 6 | Hardcoded password literal. | Remove unused SYNC_PASSWORD; no synchronization feature needs it. |
| W0718 | Quality | 34 | Catching Exception hides unexpected programming errors. | Catch KeyError for a missing contact; allow unrelated failures to surface. |
| W1514 | Portability | 54 | CSV output relies on the platform default encoding. | Specify encoding="utf-8"; keep newline="" for CSV. |
| C0200 | Quality | 49-50 | range(len(names)) requires repeated indexing. | Use enumerate(names, start=1) and access the contact by name. |
| C0103 | Naming | 10-65 | camelCase function and argument names. | Use snake_case consistently in definitions and all calls. |
| C0114 / C0116 | Documentation | 1; 10-70 | Module and function docstrings are missing. | Describe module purpose and every function contract. |
| E225 | Formatting | 23 | Missing spaces around assignment. | Change found=[] to found = []. |
| E303 | Formatting | 47 | Three blank lines before a top-level function. | Keep two blank lines between top-level functions. |
| E231 | Formatting | 84 | Missing space after a comma. | Insert the missing space before sorted(restored). |
| E501 | Formatting | 85 | A line has 86 characters, beyond Flake8 limit 79. | Wrap the final print call using parentheses. |
