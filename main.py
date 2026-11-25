"""Entry for the make.fun bounty "The Word You'd Delete From the Dictionary".

The single word to erase from the dictionary forever: irregardless.
"""

import os

ENTRY = "irregardless"


def main():
    """Validate the entry word and write it to /output/entry.txt."""
    word = ENTRY
    if not word or word.strip() == "":
        raise ValueError("entry must not be blank")
    if len(word) < 1 or len(word) > 77:
        raise ValueError("entry must be 1 to 77 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word (no whitespace inside)")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must contain no whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
