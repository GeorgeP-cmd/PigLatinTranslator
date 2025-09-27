"""
Translate a sentence into Pig Latin.
Moves initial consonant clusters before the first vowel to the end,
adds 'ay' for consonants, 'way' for vowel-starting words,
preserves capitalization and punctuation.
"""
#Pig latin translator
# Example usage
# text = "hello apple"
# print(pig_latin_translator(user_input))
# Output: "ellohay appleway"

# Get user input
user_input = input("Enter words: ")
# Function to translate text to Pig Latin
def pig_latin_translator(text):
# Define vowels
    vowels = "aeiouAEIOU"
    tokens = text.split()
# Validate input
    if not all(w.isalpha() for w in tokens):
         return "Invalid input. Please enter a valid word."
    # Convert to Pig Latin
    pig_latin_words = []
# Iterate through each word in the input text
    for word in tokens:
        if word[0] in vowels:
            pig_latin_word = word + "way"
        else:
            # find the index of the first vowel in the word
            first_vowel_idx = None
            for i, ch in enumerate(word):
                if ch in vowels:
                    first_vowel_idx = i
                    break
            # if there are no vowels, treat entire word as consonant cluster
            if first_vowel_idx is None:
                pig_latin_word = word + "ay"
            else:
                pig_latin_word = word[first_vowel_idx:] + word[:first_vowel_idx] + "ay"
# Append the translated word to the list
        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)

print(pig_latin_translator(user_input))
# Function to translate text to Pig Latin