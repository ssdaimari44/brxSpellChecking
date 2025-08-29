import streamlit as st
from src.spell_checker import SpellChecker

# Load spell checker
DICT_PATH = "data/hindi_dictionary.txt"
spell_checker = SpellChecker(DICT_PATH)

st.title("Bodo Spell Checker")

# Textbox for input
text_input = st.text_area("Enter Hindi text:", "मुझे पढाई पसन्द है")

if st.button("Check Spelling"):
    results = spell_checker.check_paragraph(text_input)

    if not results:
        st.success("✅ No spelling errors found!")
    else:
        for word, suggestions in results.items():
            suggestion_text = ", ".join([sug for sug, dist in suggestions])
            st.error(f"❌ {word} → Suggestions: {suggestion_text}")
