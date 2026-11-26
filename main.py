"""Entry for the make.fun bounty "The Word You'd Delete From the Dictionary".

The single word to erase from the dictionary forever: unthaw.

Why this word: "unthaw" argues with itself. "Un-" means to reverse,
and "thaw" means to melt — so "unthaw" should mean "to freeze". But
the dictionary says it means "to thaw", the exact thing it claims to
undo. It is the one word that cannot decide what it means, and every
time someone uses it, half the room hears the opposite. Deleting it
removes the only word that means its own opposite.
"""

import os

ENTRY = "unthaw"

# Why this word earns deletion: a self-contradicting word. "Un-" plus
# "thaw" should mean "to freeze", yet the dictionary says it means
# "to thaw" — the exact thing it claims to undo.
REASON = "a word that means its own opposite"


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
    # A dictionary headword is letters only: digits or punctuation
    # would make it a code or an abbreviation, not a word to delete.
    if not word.isalpha():
        raise ValueError("entry must be letters only (a dictionary word)")
    # Dictionary headwords are lowercase; a capital would be a name,
    # and a name is not the kind of word this bounty deletes.
    if word != word.lower():
        raise ValueError("entry must be lowercase (dictionary headword form)")
    # Two runs write byte-identical output, "unthaw" (6 chars).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
