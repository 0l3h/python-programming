import nltk
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

text = nltk.corpus.gutenberg.words('burgess-busterbrown.txt')
text_string = ' '.join(text)

def count_words(text):
    words = nltk.word_tokenize(text)
    return len(words)

def most_used_words(text, stop_words):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    cnt = Counter(words)
    most_common = cnt.most_common(10)
    x = [word for word, _ in most_common]
    y = [count for _, count in most_common]

    return x, y

total_words = count_words(text_string)
stop_words = set(stopwords.words('english'))
x_original, y_original = most_used_words(text_string, stop_words)

plt.figure(figsize=(10, 6))
plt.bar(x_original, y_original, color='skyblue')
plt.title("10 найбільш вживаних слів у тексті (оригінал)")
plt.xlabel("Слова")
plt.ylabel("Зустрічаються разів у тексті")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

x_cleaned, y_cleaned = most_used_words(text_string, stop_words)

plt.figure(figsize=(10, 6))
plt.bar(x_cleaned, y_cleaned, color='lightcoral')
plt.title("10 найбільш вживаних слів у тексті (без стоп-слів)")
plt.xlabel("Слова")
plt.ylabel("Зустрічаються разів у тексті")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
