#laba4 "Робота з рядками"
# Завдання 1. Генератор речень
import random
noun = ["Steve ", "Garett ", "Natalie ", "Henry ", "Dawn "]
verb = ["is walking", "is mining", "is fighting", "is crafting", "is building"]
place = [" in the nether", " with flint and steel", " with chicken jockey", " in the village", " in a woodland mansion"]
a = random.randint(0,4)
b = random.randint(0,4)
c = random.randint(0,4)
print(noun[a] + verb[b] + place[c], end = " ")
print()

#Завдання 2. Аналіз тексту по символах і словах
file_path = "python_crap/hamlet.txt"

def symbols(filePath):
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    nospaces = len(text) - text.count(" ")
    print(f"The number of symbols with spaces: {len(text)}")
    print(f"The number of symbols without spaces: {nospaces}")


def words(filePath):
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    text = text.casefold()
    words = text.split()
    dictionary = dict()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    print(f"The amount of words in this text: {len(text.split(" "))}")
    print(f"The amount of different words without repeating: {len(dictionary)}")
    # print(dictionary)
    #print(dictionary.values())
    countUnique = 0
    for values in dictionary.values():
        if values == 1:
            countUnique += 1
    print(f"The amount of unique words: {countUnique}")

symbols(file_path)
words(file_path)

#Завдання 3. Знаходження емоційно забарвлених слів у тексті

def occurances(filePath):
    oldEnglish = ["being", "thee", "thou", "hath", "shall", "till", "hamlet", "virtue", "prepare", "thyself"]
    positive = ["good", "welcome", "well", "love", "pardon", "heaven", "true", "affection", "angels", "faith"]
    negative = ["fear", "last", "death", "revenge", "devil", "hell", "alas", "false", "prison", "cry", "grief"]
    file = open(filePath, 'r', encoding="utf-8")
    text = file.read()
    words = len(text.split(' '))
    words = text.strip()
    words = words.lower()
    p1 = dict()
    p2 = dict()
    p3 = dict()

    for word in words.split(' '):
            for detection in oldEnglish:
                if detection in p1:
                    if detection == word:
                        p1[detection] += 1
                else:
                    p1[detection] = 0
            for detection in positive:
                if detection in p2:
                    if detection == word:
                        p2[detection] += 1
                else:
                    p2[detection] = 0
            for detection in negative:
                if detection in p3:
                    if detection == word:
                        p3[detection] += 1
                else:
                    p3[detection] = 0
    for i in p1:
            print(f"The word \"{i}\" occurs in {p1[i]} instances!")
    for i in p2:
            print(f"The word \"{i}\" occurs in {p2[i]} instances!")
    for i in p3:
            print(f"The word \"{i}\" occurs in {p3[i]} instances!")

occurances(file_path)