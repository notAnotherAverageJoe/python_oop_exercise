import random

class WordFinder:
    """A class to read a file containing words and provide random words."""

    def __init__(self, file_path):
        """Initialize the WordFinder with a path to a file containing words."""
        self.words = self.read_words(file_path)

    def read_words(self, file_path):
        """Read words from the file and return them as a list."""
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]
        print(f"{len(words)} words read")
        return words

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

# Instantiate WordFinder after its definition
wf = WordFinder("words.txt")  