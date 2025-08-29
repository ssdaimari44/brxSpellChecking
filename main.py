from src.spell_checker import SpellChecker
if __name__ == "__main__":
    dict_path = "data/hindi_dictionary.txt"
    spell_checker = SpellChecker(dict_path)

    # Example: misspelled Hindi word
    word = "पrई "   # missing "ढ़"
    suggestions = spell_checker.suggest(word)

    print(f"Input: {word}")
    print("Suggestions:")
    for suggestion, dist in suggestions:
        print(f"  {suggestion} (distance: {dist})")