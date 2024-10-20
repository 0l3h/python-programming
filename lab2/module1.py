import math

def multiply_even():
    n = int(input("Введіть натуральне число n, більше 1: "))
    product = 1
    if(n <= 1):
        print("Некоректне значення n")
        return None
    else:
        for i in range(2, n+1):
            if(i % 2 == 0):
                product *= i
        return product
