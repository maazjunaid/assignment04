import string

def word_frequency(text):
    text = text.lower()
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def display_word_frequencies(word_freq):
    print("Word Frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

user_input = input("Enter some text: ")
word_freq = word_frequency(user_input)
display_word_frequencies(word_freq)