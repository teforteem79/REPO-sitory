#laba1.py
import math
import random

#Завдання 1) Вираз з умовою
print("Завдання 1:\n")
print("Ваша кусково-задана функція: ")
print("z = {xy + y,  y < 10")
print("    {x + y^e, y >= 10")
x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))

if y < 10:
    z = x*y + y

if y>=10:
    z = x + pow(y,math.e)

print(f"z = {z}")
print()

#Завдання 2) Знайти найбільший спільний дільник чисел x та y
print("Завдання 2:\n")
x1 = x
y1 = y
if x>y:
    while y != 0:
        temp = y #y=36 temp=36
        y = x%y #y = 20
        x = temp #x = 36
    print(f"{x} - Найбільший спільний дільник чисел {x1} та {y1}!")
else:
    while x != 0:
        temp = x #x=36 temp=36
        x = y%x #x = 20
        y = temp #y = 36
    print(f"{y} - Найбільший спільний дільник чисел {x1} та {y1}!")
print()
#Завдання 3)  Дано двовимірний масив розмірністю 4х6, заповнений цілими числами.
             #Сформувати одномірний масив, кожний елемент якого дорівнює найбільшому
             #елементу відповідного рядка.
print("Завдання 3:\n")
r = 4 # рядки
c = 6 # стовпці
a = [[0] * c for i in range(r)]

print("Двовимірний масив, заповнений випадковими цілими числами:")

for i in range(r):
    for j in range(c):
        a[i][j] = random.randint(1, 9)
for row in a:
    print(' '.join([str(elem) for elem in row]))

print("Одновимірний масив із максимальних значень відповідних рядків:")
for i in range(r):
    b = max(a[i])
    print(b, end=" ")