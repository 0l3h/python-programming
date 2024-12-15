import nltk
import string
import numpy as np
import re
import matplotlib.pyplot as plt
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('gutenberg')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

text = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
text_string = ' '.join(text)

with open('nltk_results.txt', 'w') as write_file:
    # Токенізація
    sentences = nltk.sent_tokenize(text_string)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
    print(words)
    write_file.write(' '.join(words) + '\n')

    # Стеммінг
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    for w in words:
        rootWord=ps.stem(w)
        print(rootWord)
        write_file.write(rootWord + '\n')

    # Лематизація
    wordnet_lemmatizer = WordNetLemmatizer()
    tokenization = nltk.word_tokenize(text_string)

    for w in tokenization:
        print("Лема {}: {}".format(w, wordnet_lemmatizer.lemmatize(w)))
        write_file.write("Лема {}: {}".format(w, wordnet_lemmatizer.lemmatize(w)) + '\n')

    # Видалення стоп-слів
    stop_words = set(stopwords.words("english"))
    words = nltk.word_tokenize(text_string)
    without_stop_words = [word for word in words if not word in stop_words] 
    print(without_stop_words)
    write_file.write(' '.join(without_stop_words) + '\n')

    # Видалення пунктуації
    l = nltk.word_tokenize(text_string)
    ll = [x for x in l if not re.fullmatch('[' + string.punctuation + ']+', x)]

    print(ll)
    write_file.write(" ".join(ll) + '\n')
