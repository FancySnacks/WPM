from __future__ import annotations

import random


class WordSequence:
    def __init__(self):
        self._full_sequence: str = ""

        self.words = ["tomato",
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

    @property
    def sequence(self) -> str:
        return self._full_sequence

    def generate_sequence(self, word_count: int):
        self._full_sequence = ' '.join(random.choices(self.words, k=word_count))

    def load_words_from_file(self, path: str):
        with open(path, "r") as file:
            words = file.readlines()
            self.words = words
