n = int(input("Введіть кількість елементів (<= 1000): "))
end = n

if(n <= 1000):
    s = {i ** 2 for i in range(1, n+1)}
    print(s)
else:
    print("Введене число більше 1000")
