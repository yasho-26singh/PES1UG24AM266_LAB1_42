# Lab 6: Code and Branch Coverage Analysis

**Name:** Shreya Yashodhara Singh  
**SRN:** PES1UG24AM266  
**Assigned application:** 27 - Traffic Fine

The supplied assignment spreadsheet maps this SRN to [SETAPESU26/L6_L7_27_traffic_fine](https://github.com/SETAPESU26/L6_L7_27_traffic_fine). The application and starter tests match the assigned source exactly. Source application blob: `63130ef04debd928aaab213c0830d90b2688b1d5`; starter test blob: `22d2e1bc047892ac8ef7725be83c2735cb920740`.

## Measured results

| Suite | Tests passed | Statements covered | Branch outcomes covered | Coverage.py score |
| --- | ---: | ---: | ---: | ---: |
| Starter, line mode | 2 | 9/35 (25.71%) | Not measured | 26% |
| Starter, branch mode | 2 | 9/35 (25.71%) | 4/26 (15.38%) | 21% |
| Code coverage | 14 | 35/35 (100%) | Not measured | 100% |
| Branch coverage | 71 | 35/35 (100%) | 26/26 (100%) | 100% |

All suites together: **87 passed**. Coverage is restricted to `traffic_fine.py`. Coverage.py's branch-mode score combines statements and branch outcomes; the branch percentage is reported separately above. There are no exclusions, missing statements, missing branches, or partial branches in the final branch run.

## Submission files

- [CodeCoverageTest_traffic_fine.py](CodeCoverageTest_traffic_fine.py)
- [BranchCoverageTest_traffic_fine.py](BranchCoverageTest_traffic_fine.py)
- [Coverage analysis](coverage_analysis.md)
- [Code output image](evidence/code_coverage_output.png) and [command log](evidence/code_terminal_output.txt)
- [Branch output image](evidence/branch_coverage_output.png) and [command log](evidence/branch_terminal_output.txt)
- [Code coverage JSON](evidence/code_coverage.json), [branch coverage JSON](evidence/branch_coverage.json), and [all-tests result](evidence/all_tests.txt)

The images are screenshots of a browser transcript viewer showing verbatim output from real command executions. They are not native terminal-window captures. Initial measurements are provided as text and JSON; only final results above 90% are pictured. Native terminal screenshots can be captured after running the commands below if the evaluator requires that exact presentation.

## Reproduce

Run inside `Lab6` using Python 3.12:

```sh
python -m pip install -r requirements.txt
python -m coverage run --source=traffic_fine -m pytest -q CodeCoverageTest_traffic_fine.py
python -m coverage report -m --fail-under=90
python -m coverage run --branch --source=traffic_fine -m pytest -q BranchCoverageTest_traffic_fine.py
python -m coverage report -m --fail-under=90
python -m pytest -q
```

`pytest.ini` enables discovery of both required capitalized filenames. Each coverage run replaces the prior measurement. The submission is split into a code-coverage commit and a branch-coverage commit. This work follows the supplied Lab 6 handout; the spreadsheet also mentions Lab 7, for which no handout was supplied.
