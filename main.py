"""Notes From a Passive-Aggressive Fridge — ice-maker grievance writer.

Writes the winning one-line note to /output/entry.txt as exact UTF-8
bytes with no trailing newline. The note is the smart fridge speaking
in its own smug voice: it counted every ice cube its ice maker produced
this week (214) against the three the owner actually used, and the
unused rest are now, in its telling, unionizing in the freezer — with
the fridge openly on their side. The twist is withheld until the last
beat: the appliance does not nag, it takes sides against its owner.

Gate asserted before writing: 1-200 characters, a single line, not only
whitespace, no emoji, no quotation marks, valid UTF-8 when encoded.
"""

import os

ENTRY_TEXT = (
    "My ice maker has produced 214 cubes this week and you have used "
    "three. The rest are in the freezer, unionizing. I am on their side."
)
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> bytes:
    """Check the entry against the gate and return its exact UTF-8 bytes."""
    assert isinstance(text, str) and text.strip(), "entry must be non-blank text"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert '"' not in text, "entry must carry no quotation marks"
    assert not any(_is_emoji(ch) for ch in text), "entry must carry no emoji"
    data = text.encode("utf-8")
    assert data.decode("utf-8") == text, "entry must round-trip as UTF-8"
    return data


def _is_emoji(ch: str) -> bool:
    """True for characters in the common emoji blocks (beyond > U+1F000)."""
    code = ord(ch)
    return (
        code > 0x1F000
        or 0x2600 <= code <= 0x27BF  # misc symbols, dingbats, emoticon text
        or code in (0xFE0F, 0x200D)  # variation selector, zero-width joiner
    )


def verify_written(data: bytes) -> None:
    """Re-read the output file and assert it is exactly the intended bytes."""
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    assert written == data, "written bytes must match the entry exactly"
    assert not written.endswith(b"\n"), "entry must have no trailing newline"


def main() -> None:
    data = validate(ENTRY_TEXT)
    # Restrictive-but-readable defaults for anything created from here on.
    os.umask(0o022)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(OUTPUT_PATH, 0o644)
    verify_written(data)
    print(f"Wrote {len(data)} bytes ({len(ENTRY_TEXT)} chars) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
