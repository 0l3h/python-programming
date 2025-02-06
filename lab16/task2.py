import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

text = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
text_string = ' '.join(text)

with open('nltk_results.txt', 'w') as write_file:
    # Токенізація
    sentences = nltk.sent_tokenize(text_string)
    all_words = []

    # Стеммінг
    ps = PorterStemmer()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        stemmed_words = [ps.stem(w) for w in words]
        all_words.extend(stemmed_words)

    # Лематизація
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized_words = [wordnet_lemmatizer.lemmatize(w) for w in all_words]

    # Видалення стоп-слів
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in lemmatized_words if word not in stop_words]

    # Видалення пунктуації
    final_words = [word for word in filtered_words if word not in string.punctuation]

    final_text = ' '.join(final_words)

    print(final_text)
    write_file.write(final_text + '\n')
