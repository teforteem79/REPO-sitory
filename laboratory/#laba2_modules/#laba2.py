import MoyaFunkciya as mf

print("Завдання 1. Демонстрація алгоритму швидкого сортування:")
#Введення власного масиву даних цілочисельного типу:
n = int(input("Enter the max size of list: "))
custom = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
print("Initial array:")
print(custom)
print("Quicksorted array:")
print(mf.quicksort(custom))
print("Reverse Quicksorted array:")
print(mf.reversequicksort(custom))

print("Завдання 2. Пошук елемента за значенням:")
ListOfRandomShit = ["apple", 17, "tree", 120, 193.5, 35.8, 18, "table", "сонечко", "pi"]
print("List of your elements:")
print(ListOfRandomShit)
mf.searchfor(ListOfRandomShit)

print("Завдання 3. Пошук послідовності елементів:")
dom = ['1', '2', '3', '4', '5', '6', '7', '8']
sub = ['3', '4', '5']
print(f"Main array: {dom}")
print(f"Sequence which will be found: {sub}")
print(f"The presence of your sequence in a given list is: {mf.findsequence(sub, dom)}")

print("Завдання 4. Пошук перших п'яти мінімільних елементів:")
n = int(input("Size of list: "))
custom = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
print(custom)
mf.minmal5(custom)

print("Завдання 5. Пошук перших п'яти максимальних елементів:")
n = int(input("Size of list: "))
custom = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
print(custom)
mf.maximal5(custom)

print("Завдання 6. Знаходження середнього арифметичного:")
n = int(input("Size of list: "))
custom = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
print(f"Середнє арифметичне ваших чисел: {mf.avg(custom)}")

print("Завдання 7. Ліквідація повторів у масиві")
n = int(input("Enter the max size of list: "))
custom = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
mf.norepeats(custom)

