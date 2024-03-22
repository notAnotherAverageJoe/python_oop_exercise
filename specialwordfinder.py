from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that filters out blank lines and comments."""

    def read_words(self, file_path):
        """Read words from the file, filtering out blank lines and comments."""
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        print(f"{len(words)} words read")
        return words
