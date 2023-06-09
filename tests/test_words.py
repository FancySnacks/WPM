import pytest

from wpm.WordSequence import WordSequence

@pytest.fixture
def temp_txt_file(tmp_path):
    filename = 'example.txt'
    path = str(tmp_path) + filename
    words = ['animal', 'burrito', 'chess', 'poster', 'music', 'railway']

    with open(path, 'x') as f:
        f.write('\n'.join(words))

    return path


def test_words_are_loaded_from_file_correctly(temp_txt_file):
    sequence = WordSequence.generate_sequence_from_file(temp_txt_file)

    assert len(sequence) > 0
    assert all([isinstance(word, str) for word in sequence]) is True
