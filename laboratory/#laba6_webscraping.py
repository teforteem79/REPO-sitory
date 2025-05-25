#laba 6 "Збір даних з веб-документів за допомогою мови Python"
from bs4 import BeautifulSoup as КрасиваЗупа
import requests
import matplotlib.pylab as plb

#відкриття сайту і форматування даних

url = "https://uk.wikipedia.org/wiki/Любешівський_район"
request = requests.get(url)
print(request)
tpage = request.content
soup = КрасиваЗупа(tpage, 'html.parser')
text = soup.find_all(string=True)
stringtext = ""
for pmo in text:
    stringtext += "{} ".format(pmo)
    words = stringtext.split()


#підрахунок частоти появи html-тегів, посилань і зображень

hyperlinks = []
for hyperlink in soup.find_all('a'):
    hyperlinks.append(hyperlink.get('href'))
images = soup.find_all('img')
tags = soup.find_all()
print(f"Кількіть гіперпосилань на сайті: {len(hyperlinks)}")
print(f"Кількіть зображень на сайті: {len(images)}")
print(f"Кількіть html-тегів на сайті: {len(tags)}")

#підрахунок частоти слів

afterisalpha = []
occurance = dict()
for word in words:
    if word.isalpha():
        afterisalpha.append(word)
for word in afterisalpha:
    if word in occurance:
        occurance[word] += 1
    else:
        occurance[word] = 1
print(occurance)

#графік для частоти тегів
y = ['li', 'p', 'script', 'header', 'footer', 'img']
li = len(soup.find_all('li'))
p = len(soup.find_all('p'))
html = len(soup.find_all('html'))
head = len(soup.find_all('head'))
title = len(soup.find_all('title'))
script = len(soup.find_all('script'))
header = len(soup.find_all('header'))
footer = len(soup.find_all('footer'))
a = len(soup.find_all('a'))
img = len(soup.find_all('img'))
x = [li, p, script, header, footer, img]
plb.title("частота появи деяких тегів")
plb.xlabel("кількість")
plb.ylabel("теги")
for i in range(1,11):
    plb.xticks(x)
plb.barh(y,x, color = "black")
plb.grid(axis="x")
plb.show()
