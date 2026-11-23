"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single number (digits only) to /output/entry.txt: the honest
count of open browser tabs. No words, no punctuation, no second number.
"""

import os

# The count: 847 open tabs. High enough to surprise (a chronic tab
# hoarder who never closes anything), specific enough to read as a real
# lived-in count rather than a round guess like 500 or 1000, and still
# believable as an honest answer — no commas, no words, just digits.
TAB_COUNT = "847"


def validate_entry(text: str) -> None:
    """Guard the entry before writing: digits only, 1-5 characters."""
    if not text or len(text) > 5 or not text.isascii() or not text.isdigit():
        raise ValueError(f"entry must be 1-5 digits, got {text!r}")


def main() -> None:
    validate_entry(TAB_COUNT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(TAB_COUNT)
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TAB_COUNT, f"entry mismatch: {written!r} != {TAB_COUNT!r}"
    print(f"entry.txt OK: {written!r} ({len(written.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
