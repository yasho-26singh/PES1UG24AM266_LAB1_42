# Reflection

Shreya Yashodhara Singh | PES1UG24AM266

**Draft for student review:** The supplied handout refers to reflection questions but does not list them. These four prompts address the lab learning outcomes; they are not quoted instructor questions or a claim of personal experience.

## 1. How do the three tools complement one another?

Pylint identified maintainability problems such as broad exception handling, missing documentation and naming. Bandit detected security-sensitive patterns, including pickle deserialization and MD5. Flake8 identified spacing, blank-line and line-length violations. Using all three covered different aspects of the same source file.

## 2. Which findings mattered most, and why?

Unsafe pickle loading was the most direct risk because a modified backup could cause code execution when loaded. Bandit marked MD5 as High and pickle loading as Medium, so both were addressed first. Here the hash is only a display ID; replacing MD5 does not turn a six-character ID into a secure or collision-free identifier.

## 3. What tradeoffs and challenges arose while fixing the program?

Replacing pickle required changing both backup and restore together. JSON preserves the string-and-dictionary contact data, but existing pickle backups cannot be loaded by the new code. Narrowing the exception to KeyError preserves the missing-contact message while exposing unexpected TypeError failures. Renaming functions required updating every demonstration call.

## 4. How were the fixes verified, and what are the limits of static analysis?

The final source passed all three tools and 12 regression checks. The demo output matches the baseline except for the deliberately changed SHA-256 display ID. Tests cover normal and invalid input, search, city changes, CSV quoting and Unicode, and backup round trips. Clean tool output does not prove correctness or security; JSON content is not schema-validated, CSV fields are not neutralized for spreadsheet formulas, and more realistic applications would need stronger input and file protections.

