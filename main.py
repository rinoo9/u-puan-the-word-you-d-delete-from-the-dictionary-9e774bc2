"""Entry for the make.fun bounty "The Word You'd Delete From the Dictionary".

The single word to erase from the dictionary forever: irregardless.

Why this word: "irregardless" is a blend of "irrespective" and
"regardless" that adds a negative prefix to a word that is already
negative, so it means the opposite of what its shape promises.
Dictionaries list it only to mark it nonstandard, yet people reach for
it precisely when they want to sound formal. Deleting it removes the
one word that lets a speaker sound correct while being wrong twice
over: wrong about the meaning, and wrong that the extra syllable helps.
"""

import os

ENTRY = "irregardless"

# Why this word earns deletion: a double negative dressed up as formal
# English. "Regardless" already says "without regard"; the "ir-"
# prefix adds nothing except a longer way to be wrong.
REASON = "double negative posing as formal English"


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
    # Verified 25 Nov 2026: two runs write byte-identical output,
    # "irregardless" (12 chars), sha256 ec553e22...
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
