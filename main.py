"""The Robot Apology — entry program.

Writes a two-line robot confession to /output/entry.txt.
Deterministic: the text is fixed, so every run produces identical bytes.
"""

from pathlib import Path

ENTRY = (
    "I'm sorry I watered the plastic plant every morning for a month while the real fern beside it wilted.\n"
    "I've learned to check for roots before I pour, so now I touch the soil before I trust my eyes.\n"
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
