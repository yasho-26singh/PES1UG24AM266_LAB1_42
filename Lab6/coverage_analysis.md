# Coverage analysis

Shreya Yashodhara Singh | PES1UG24AM266

## Coverage concepts

Statement coverage asks whether executable statements ran. Branch coverage checks alternative control-flow outcomes, including decisions and loop entry/exit. Every statement can run while some decision outcomes remain untested. Path coverage concerns complete sequences of decisions; function coverage concerns whether each function was called. The measured metrics here are statement and branch coverage.

## Initial tests

The two supplied tests check no speeding and a clean licence record. They execute 9/35 statements (25.71%) and 4/26 branch outcomes (15.38%). The branch-mode combined score is 21%. Untested behavior includes speeding fine bands, zone selection, licence actions above the clean-record range, and all penalty aggregation logic.

## Code coverage suite

Four speeding cases reach the no-fine return, school/highway/default bases, doubled fine and tripled fine. Six licence cases cover revoke, both suspension routes, warning, notice, and no action. Three aggregation cases cover empty input, summation and the cap; a negative-fine case checks the exception. Input-list assertions verify that totals do not mutate their inputs.

The 14 cases execute 35/35 statements: 100% statement coverage.

## Branch coverage suite

| Area | Cases and expected behavior |
| --- | --- |
| Speeding thresholds | For each zone, excess -1 and 0 produce zero; 1 and 20 use base; 21 and 40 use twice base; 41 uses three times base |
| Zone decisions | School base=2000; highway base=1000; city and rural exercise the default base=500 |
| Licence thresholds | Points 0, 3, 4, 7, 8, 11, 12, 13 across all combinations of commercial status and repeat offending |
| Licence precedence | At 12+ points commercial status determines revoke versus suspend; at 8-11 repeat offending determines suspend versus warning |
| Total loop | Empty, singleton, and multiple-item lists exercise skipped and repeated iterations |
| Cap | 9999 stays below cap; 10000 remains exact; 10001 becomes 10000, including through multiple fines |
| Invalid fines | Negative fine first, after a positive fine, and after a subtotal above the cap all raise ValueError |

The 71 cases cover 35/35 statements and 26/26 branch outcomes, with zero partial branches. All 87 tests, including the supplied starter cases, pass together. All three application functions are called, but a separate function-coverage percentage is not reported.

## Interpretation

Both final coverage measures exceed the handout's 90% thresholds. Threshold equality cases catch common `>` versus `>=` errors. Testing all flag combinations checks decision precedence, and rejecting a negative fine after exceeding the cap guards against an incorrect early return. No application changes, branch exclusions, or artificial coverage suppression were used.

100% branch coverage does not prove all paths or arbitrary input types correct. Tests follow the supplied code's behavior; they do not claim that its fine values represent current traffic laws. Evidence PNGs display real command output through a transcript viewer; text logs and JSON retain inspectable measurements.
