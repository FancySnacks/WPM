"""Creates word sequences"""

from __future__ import annotations

import random

from wpm.const import DEFAULT_WORDLIST_PATH


class WordSequence:
    words = ["tomato",
             "library",
             "torch",
             "dungeon",
             "chips",
             "shotgun",
             "giraffe",
             "coffee",
             "railway",
             "skeleton",
             "book",
             "zombie",
             "dracula",
             "soda",
             "movie",
             "pistol",
             "bullets",
             "ammo",
             "python",
              ]

    @classmethod
    def _create_sequence(cls, words: list[str], word_count: int) -> str:
        if word_count > len(words):
            word_count = len(words)

        full_sequence: str = ' '.join(random.choices(words, k=word_count))
        return full_sequence

    @classmethod
    def generate_sequence_from_file(cls, path: str = DEFAULT_WORDLIST_PATH):
        with open(path, "r") as file:
            words = file.readlines()

        return cls._create_sequence(words, 6)

    @classmethod
    def generate_sequence(cls):
        return cls._create_sequence(cls.words, 6)
