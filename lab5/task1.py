print("Ввведіть натуральне число N: ", end="")
N = int(input())
numbers = []

if (N <= 0):
    print("Число N повинно бути більше нуля")
else:
    for i in range(N):
        print("\nВведіть ", i+1, "-й елемент: ", end="", sep="")
        n = float(input())
        numbers.append(n)

    for n in numbers:
        if n > 0:
            print(n)
