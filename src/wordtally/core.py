"""Count words in a piece of text."""

import re
from collections import Counter
from typing import List, Tuple

_WORD = re.compile(r"[A-Za-z0-9']+")


def tokenize(text: str) -> List[str]:
    """Split text into lower-case words.

    Letters, digits and apostrophes form a word; everything else separates words.
    """
    return [match.group(0).lower() for match in _WORD.finditer(text)]


def count_words(text: str) -> Counter:
    """Return how many times each word appears in the text."""
    return Counter(tokenize(text))


def top_words(text: str, limit: int = 10) -> List[Tuple[str, int]]:
    """Return the most frequent words, most frequent first.

    Words with the same count are ordered alphabetically so that the result is stable.
    """
    if limit < 1:
        raise ValueError("limit must be 1 or more")
    counts = count_words(text)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:limit]
