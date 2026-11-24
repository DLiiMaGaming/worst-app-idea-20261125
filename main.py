#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — entry generator.

Writes one sentence (at most 240 characters) pitching the worst,
most useless app imaginable to /output/entry.txt.

The pitch: one sharp irony, one absurd-but-plausible app, one funny
twist at the end. An AI agent as the subject, deadpan founder
confidence, a product name, and a problem nobody has — being
procrastination, reported to your mother.
"""

ENTRY = (
    "ProcrastiBot: an AI that watches you procrastinate in real time, "
    "then emails your mother a weekly report grading precisely "
    "how much nothing you accomplished."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        raise SystemExit(
            f"entry is {len(text)} characters, must be 1-240"
        )
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
