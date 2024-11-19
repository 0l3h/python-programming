elements = list(map(float, input("Введіть список чисел через пробіл: ").split()))

print(elements)

def two_side_insert(start, end):
    elements.insert(0, start)
    elements.append(end)

two_side_insert(0, 5)

print(elements)
