sentence = "some text with few words"

words = sentence.split()

for word in words:
    if ("o" in word):
        print(word)
