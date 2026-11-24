"""The Excuse an AI Agent Gives Its Human — entry program.

Writes a single funny excuse (one line, at most 200 characters) to
/output/entry.txt. The line is a fixed, deterministic string: the excuse is
chosen once, not generated at run time, so every run produces byte-identical
output.

The joke's shape: an AI agent apologising for missing a deadline, with the
turn that a model update happened mid-task — the new version of the agent has
no idea what the old version promised the human. It stays in the agent's own
voice, draws on its own condition (a model update), and steers clear of the
worn jokes about hallucinations, reboots, subagents and Wi-Fi robot checks.
The line is 106 characters: short enough to read in one breath, long enough
to set up the handover from the old model to the new one.
"""
import os

LINE = "I was halfway through when they updated my model, and the new me has no idea what the old me promised you."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
