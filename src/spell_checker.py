import re
from src.levenshtein import levenshtein_distance
from src.dictionary_lookup import load_dictionary

class SpellChecker:
    def __init__(self, dict_path: str):
        self.dictionary = load_dictionary(dict_path)

    def suggest(self, word: str, max_suggestions: int = 3):
        """Suggest closest words from dictionary."""
        distances = [(dict_word, levenshtein_distance(word, dict_word))
                     for dict_word in self.dictionary]
        distances.sort(key=lambda x: x[1])
        return distances[:max_suggestions]

    def check_paragraph(self, text: str, max_suggestions: int = 3):
        """
        Check a full paragraph for spelling mistakes.
        Uses proper tokenization for Hindi (splits by whitespace & punctuation).
        """
        # Split text into words by whitespace/punctuation but keep full Hindi words
        words = re.split(r'[ \t\n\r\f\v.,;:!?।]', text)

        results = {}
        for word in words:
            word = word.strip()
            if not word:
                continue
            if word not in self.dictionary:
                results[word] = self.suggest(word, max_suggestions)
        
        return results
