word1 = "hello"
word2 = "world"

new_str = ''.join({word1, word2})

for char in new_str:
    if(new_str.count(char) == 1):
        print(char)
