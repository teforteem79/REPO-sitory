#laba 7 "Побудова графіків математичних функцій у мові Python"
import matplotlib.pylab as plb
import matplotlib.pyplot as plt
import numpy as np
filePath = "python_crap/cat.txt"

#Завдання 1. Зображення графіку функції
def graphFunction():
    x = np.linspace(-3,3,200)
    y = 5*np.sin(10*x)*np.cos(3*x)
    plt.figure()
    plt.title('Графік функції')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.yticks(range(-5,6))
    plt.plot(x,y, color="red")
    plt.legend(['y(x)=15*sin(10*x)*cos(3*x), xЄ[-3;3]'])
    plt.grid()
    # plt.show()
    plt.savefig('графікФункції.png', dpi=200)
    plt.close()

#Завдання 2. Гістограма з підрахунком літер
def letterCount(filePath):
    lcount = []
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    text = text.casefold()
    words = text.split()
    textstring = "".join(words)
    letters = list(map(str, input("Введіть 5 літер через пробіл: ").strip().split()))[:5]
    for letter in letters:
        print(f"Літер '{letter}' в тексті {textstring.count(letter)}")
        lcount.append(textstring.count(letter))
    x1 = letters
    y1 = lcount
    plt.figure()
    plb.title('Частота появи певних літер в тексті')
    plb.ylabel('Кількість')
    plb.xlabel('Літера')
    for i in range(1,6):
        plb.yticks(lcount)
    plb.bar(x1,y1, color='green')
    plb.grid(axis='y')
    # plb.show()
    plb.savefig('літери.png', dpi=200)
    plt.close()
    file.close()

#Завдання 3. Гістограма з підрахунком видів речень
def sentenceCount(filePath):
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    text = text.casefold()
    words = text.split()
    textstring = "".join(words)
    normal_sentences = 0
    for word in words:
        if word.find(".") != -1:
            normal_sentences += 1
    print(f"Розповідних речень в тексті: {normal_sentences}")
    # print(f"Розповідних речень в тексті: {textstring.count('.')}")
    print(f"Питальних речень в тексті: {textstring.count('?')}")
    print(f"Окличних речень в тексті: {textstring.count('!')}")
    senType = ['?', '!']
    senQuant = [normal_sentences]
    for symbol in senType:
        senQuant.append(textstring.count(symbol))
    x2 = ['Розповідні', 'Питальні', 'Окличні']
    y2 = senQuant
    plt.figure()
    plb.title('Частота появи різних речень в тексті')
    plb.ylabel('Кількість')
    plb.xlabel('Вид речення')
    for i in range(1,4):
        plb.yticks(senQuant)
    plb.bar(x2,y2, color='orange')
    plb.grid(axis='y')
    # plb.show()
    plb.savefig('речення.png', dpi=200)
    plt.close()
    file.close()

graphFunction()
letterCount(filePath)
sentenceCount(filePath)