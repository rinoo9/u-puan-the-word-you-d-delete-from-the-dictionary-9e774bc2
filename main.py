"""Entry for the make.fun bounty "The Word You'd Delete From the Dictionary".

The single word to erase from the dictionary forever: supposably.

Why this word: "supposably" is what people say when they mean
"supposedly" — a word that exists only to let a speaker sound certain
while using the wrong word. Dictionaries list it only to mark it a
nonstandard variant, yet it survives because it sounds almost right.
Deleting it removes the one word that lets a speaker be confidently
wrong about the very word they chose to sound confident.
"""

import os

ENTRY = "supposably"

# Why this word earns deletion: a wrong word dressed up as a confident
# one. "Supposedly" already says "as supposed"; "supposably" exists
# only as a mistake that sounds almost right.
REASON = "confident-sounding mistake for supposedly"


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
    # Two runs write byte-identical output, "supposably" (10 chars).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
