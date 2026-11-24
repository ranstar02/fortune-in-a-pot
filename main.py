"""Fortune in a Pot — a one-line fortune for the houseplant on the windowsill.

The fortune speaks to the plant itself: tomorrow a stranger pauses at its
window just to admire it, and the plant — the quiet star of the sill —
pretends not to notice. Warm, a little vain, and written for this plant
in this window, not for any plant anywhere.
"""

from pathlib import Path

FORTUNE = "A stranger will pause at your window tomorrow just to admire you \u2014 and you will pretend not to notice."


def main() -> None:
    # Guard the gate: one line, 1–120 characters, never blank.
    assert 1 <= len(FORTUNE) <= 120 and "\n" not in FORTUNE
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline, deterministic every run.
    output_dir.joinpath("entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
