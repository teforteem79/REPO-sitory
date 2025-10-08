import pandas as pd
#variant 6
#dataframe Фільми


dani = {'Назва': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Fight Club', 'Inception', 'The Matrix', 'Forrest Gump', 'Interstellar', 'Titanic', 'Avatar', 'Gladiator', 'TLoTR: The Return of the King', 'The Silence of the Lambs', 'Goodfellas'], 
        'Режисер': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino', 'David Fincher', 'Christopher Nolan', 'Lana & Lilly Wachowski', 'Robert Zemeckis', 'Christopher Nolan', 'James Cameron', 'James Cameron', 'Ridley Scott', 'Peter Jackson', 'Jonathan Demme', 'Martin Scorsese'],
        'Рік випуску': [1994, 1972, 2008, 1994, 1999, 2010, 1999, 1994, 2014, 1997, 2009, 2000, 2003, 1991, 1990],
        'Бюджет': ['$25 million', '$6 million', '$185 million', '$8 million', '$63 million', '$160 million', '$63 million', '$55 million', '$165 million', '$200 million', '$237 million', '$103 million', '$94 million', '$19 million', '$25 million'],
        'Тривалість (хв)': [142, 175, 152, 154, 139, 148, 136, 142, 169, 195, 162, 155, 201, 118, 146],
        'Розмір файлу (ГБ)': [1.6, 2.1, 2.3, 1.9, 1.7, 2.0, 1.7, 1.8, 2.5, 2.7, 2.4, 2.0, 2.9, 1.4, 1.8],}
df = pd.DataFrame(data = dani)


def printDataFrame():
    print(df)

def deleteByIndex():
    index = int(input('Виберіть з яким індексом видалити рядок: '))
    df.drop(index, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df)

def addElement():
    def Year():
        try:
            year = int(input("Введіть рік випуску: "))
            return year 
        except ValueError:
            print('must be an integer!')
            Year()
    def Time():
        try:
            time = int(input("Введіть тривалість у хвилинах: "))
            return time 
        except ValueError:
            print('must be an integer!')
            Time()
    def File():
        try:
            fsize = float(input("Введіть розмір файлу у ГБ: "))
            return fsize 
        except ValueError:
            print('must be an integer or float!')
            File()
    def Budget():
        try:
            budget = float(input("Введіть бюджет у млн доларах: "))
            return budget 
        except ValueError:
            print('must be an integer or float!')
            Budget()
    name = input("Введіть назву фільму: ")
    director = input("Введіть режисера: ")
    df.loc[int(df.size/6)] = [name, director, Year(), '$'+ str(Budget())+ ' million', Time(), File()]
    print(df)

def sortByAttribute(zrostanna = True):
    while True:
        choice = input(f'''
За яким атрибутом сортувати? (порядок зростання: {zrostanna})
a. Змінити порядок сортування (True - зростання, False - спадання)
1. За Алфавітом (назва)
2. За Алфавітом (режисер)
3. За Роком випуску
4. За тривалістю
5. За розміром файлу\n''')
        if choice == 'a':
            if zrostanna == True:
                zrostanna = False
            else:
                zrostanna = True
            
        if choice == '1':
            print(df.sort_values('Назва', ascending=zrostanna))
            break
        if choice == '2':
            print(df.sort_values('Режисер', ascending=zrostanna))
            break
        if choice == '3':
            print(df.sort_values('Рік випуску', ascending=zrostanna))
            break
        if choice == '4':
            print(df.sort_values('Тривалість (хв)', ascending=zrostanna))
            break
        if choice == '5':
            print(df.sort_values('Розмір файлу (ГБ)', ascending=zrostanna))
            break


while True:
    choice = input('''
Виберіть операцію: 
1. Вивести фрейм
2. Додати елемент
3. Відсортувати фрейм за атрибутом
4. Видалити елемент (за атрибутом)
5. Видалити елемент (за індексом)
6. Вивести елементи за атрибутом\n''')
    if choice == '1':
        printDataFrame()
    if choice == '2':
        addElement()
    if choice == '3':
        sortByAttribute()
    if choice == '4':
        print('Видалено рядки, де розмір файлу менший за 1.8 ГБ: ')
        indices_to_drop = df[df["Розмір файлу (ГБ)"] < 1.8].index
        df.drop(indices_to_drop, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print(df)
    if choice == '5':
        deleteByIndex()
    if choice == '6':
        print("Виведено рядки, де фільми довші за 150 хвилин")
        print(df[df["Тривалість (хв)"] > 150])
