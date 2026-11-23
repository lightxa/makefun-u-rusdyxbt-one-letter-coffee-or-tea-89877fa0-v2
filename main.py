"""One Letter: Coffee or Tea -- variant 2 (tea).

The entry is exactly one letter: "B" for tea.

Why tea, and why it is the calmer and truer answer in the judge's
brief: coffee shouts, tea listens. Coffee is the loud answer, the
one everyone reaches for when they want to look awake. Tea is the
honest one, the drink you choose when nobody is watching, steeped
slowly, never rushed, and still there when the rush wears off.
A single "B" says that plainly: no noise, no performance, just the
quieter drink that outlasts the louder one.

The gate is strict: /output/entry.txt must be UTF-8 text of exactly
one character, not only whitespace. A trailing newline would make it
two characters and fail the gate, so this program writes the single
byte "B" and nothing else -- no newline, no spaces, no punctuation.
"""

LETTER = "B"


def main() -> None:
    """Write exactly one byte, "B", to /output/entry.txt."""
    import os
    from pathlib import Path

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # newline="" and no trailing newline: exactly one byte, "B".
    entry_path.write_text(LETTER, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
