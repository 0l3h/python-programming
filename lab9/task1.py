import os
import re

try:
    writeFile = open("TF10_1.txt", "w")
    readFile = open("TF10_2.txt", "w+")
except:
    print("Виникла помилка при роботі з файлами")
else:
    readFile.write(
"""qeuifh iuef324hou
weiufhwbo35e8leuherew423
iuwhev9645ouwgewer3jgwg
wqueyf4rgwf 3247 wrhgewg
25uqw2egtyvbi qpifrhq
""")

    readFile.seek(0)

    for line in readFile:
        formatted_line = re.sub(r'\d+', '', line)[:10]
        writeFile.write(formatted_line)
        print(formatted_line)

    writeFile.close()
    readFile.close()
