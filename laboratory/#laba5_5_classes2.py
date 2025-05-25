#laba5-5 класи
# Завдання 5 "Англо-український словник"
class EN_UA:
    def __init__(self):
        self.vocab = []
    
    def newWords(self, english, ukr1, ukr2, ukr3):
        word = [english, ukr1, ukr2, ukr3]
        self.vocab.append(word)

    def translation(self, word):
        for i in words.vocab:
            for word in i:
                if word == find:
                    return words.vocab[words.vocab.index(i)]
        
words = EN_UA()
answer = ' '
while answer != 'a' or answer != 'l' or answer != 't' or answer != 'e':
    print("Append new translation (a), List all words (l) or Translate a word (t), or Exit (e)?")
    answer = input('')
    if answer == 'a':
        eng = input("Введіть англійське слово: ")
        ukr1 = input("Введіть передклад українською: ")
        ukr2 = input("Введіть синонім: ")
        ukr3 = input("Введіть ще один синонім: ")
        words.newWords(eng, ukr1, ukr2, ukr3)
    if answer == 'l':
        for i in words.vocab:
            print(i)
    if answer == 't':
        find = input("Знайти переклад слова: ")
        print(words.translation(find))
    if answer == 'e':
        break
