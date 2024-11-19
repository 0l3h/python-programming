first_list=list(map(float, input("Введіть список чисел через пробіл: ").split()))
filtered_list = list(set(first_list))

print(filtered_list)
