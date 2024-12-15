import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter 

nltk.download('gutenberg')
nltk.download('punkt_tab')

text = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
text_string = ' '.join(text)

def count_words(text):
    sentences = nltk.sent_tokenize(text)
    k_words = 0

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        k_words += len(words)

    return k_words

def most_used_words(text):
    text1 = text.split()
    text1 = [word.lower().strip(string.punctuation) for word in text1 if word not in string.punctuation]
    
    cnt = Counter(text1)
    cort = cnt.most_common(10)
    x = [word for word, _ in cort]
    y = [count for _, count in cort]

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

total_words = count_words(text_string)
print(f"Всього слів у тексті: {total_words}")
most_used_words(text_string)
