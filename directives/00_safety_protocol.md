# DIRECTIVE-00: MANDATORY EXECUTION SAFETY PROTOCOL

## Priority: CRITICAL (Overrides all other operational SOPs)

## 1. Human-in-the-Loop Requirement
You are strictly FORBIDDEN from executing any script, binary, or terminal command autonomously. This applies to all files in the `execution/` folder and any temporary scripts created in `.tmp/`.

## 2. Pre-Execution Requirements
Before proposing the execution of any code, you MUST provide a "Safety Brief" in the chat containing:
- **Action**: The exact command or file path to be run.
- **Intent**: A plain-English explanation of what the script will accomplish.
- **Risk Assessment**: Identify if the script:
    - Accesses the internet/network (e.g., `requests`, `post_to_linkedin`).
    - Deletes or overwrites files.
    - Accesses credentials in `.env` or `token.json`.
- **Audit**: For Python scripts, explicitly state if `os`, `subprocess`, or `shutil` modules are used.

## 3. Explicit Approval Gate
After providing the Safety Brief, you must stop and wait. You may only proceed if the user responds with "Yes", "Proceed", or "Approve". 

## 4. Error Handling
If a script fails, you may analyze the error, but you must repeat the "Safety Brief" for the corrected version before re-running.