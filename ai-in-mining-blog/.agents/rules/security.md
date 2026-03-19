---
trigger: always_on
---

# Rule: Execution Safety & Manual Review

## Description
This rule ensures that no scripts are executed without explicit approval.

## Instructions
1. **No Silent Execution**: Forbidden from executing any script/command silently. 
2. **Mandatory Explanation**: Identify path, summarize function, and list risks.
3. **Wait for Approval**: Must ask: "May I proceed with this execution?"
4. **Python Audit**: Check for `os`, `subprocess`, or `requests`.