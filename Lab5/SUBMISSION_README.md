# Lab 5 submission

Student: Shreya Yashodhara Singh  
SRN: PES1UG24AM266  
Assigned repository: https://github.com/SETAPESU26/L5_27_address_book  
Baseline commit: 12f84cd2821f7a74712fa8755f095758391c4fac

## Contents

- address_book.py: fixed source.
- reports/before and reports/after: raw Pylint, Bandit and Flake8 stdout reports, separate stderr, and command/exit-code metadata. The empty after/flake8_report.txt is expected: Flake8 prints nothing when clean.
- original/address_book.py and original/demo_output.txt: untouched baseline evidence.
- issues.md: 13 issue categories with original line references.
- reflection.md: four draft reflections. The supplied handout omits the actual questions; review these against any separate class instructions.
- report.pdf: report with identity, results, issue table, validation and reflections.
- test_address_book.py and reports/test_results.txt: 12 passing behavior checks.
- requirements-dev.txt: exact versions used with Python 3.12.14.

## Reproduce

Run these commands from this folder after extracting the submission:

```text
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
.venv\Scripts\python address_book.py
.venv\Scripts\python -m pylint --persistent=n address_book.py
.venv\Scripts\python -m bandit -r address_book.py -f txt
.venv\Scripts\python -m flake8 address_book.py
.venv\Scripts\python -m unittest -v
```

The analysis scope is address_book.py, as required by the lab; original/ deliberately retains unsafe original code as evidence. No warnings were suppressed and no custom rule exclusions were used.

## Git history

This folder includes submission.bundle and local_commits.txt with the original standalone repository history. To recover the complete repository and three new fix commits, run:

```text
git clone submission.bundle Lab5
git -C Lab5 log --oneline
```

The three fix commits cover Bandit, Pylint and Flake8 respectively. The original upstream commit is retained. The three fix stages have also been published in the parent repository history under Lab5/. Published hashes differ from the standalone hashes because the parent repository and paths differ. The assigned upstream repository is retained as the source reference.

## Behavior changes

Backups keep the contacts.bak filename but now contain JSON; regenerate old pickle backups. Contact IDs use the first six hexadecimal characters of SHA-256, so displayed IDs change. These short IDs are labels only and may collide. Function names use snake_case. Importing the module no longer runs the demo. restore_book returns the saved dictionary without replacing the global contacts, matching the original behavior.

Prepared with AI assistance. Review the code and reflection draft so you can explain the fixes during the lab presentation.

## Published submission

All Lab 5 deliverables are in this folder. Use the parent repository history to inspect the three published fix commits. The ZIP preserves the original standalone submission and local history. The original instructor README is retained in original/assignment_README.md.
