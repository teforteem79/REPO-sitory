from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
url = "https://www.meteoblue.com/en/weather/week/lviv_ukraine_702550"
class WeatherParser:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.page_content = None
        self.request_status = None
        self.fetch_page()

    def fetch_page(self):
        response = requests.get(self.url)
        self.request_status = response.status_code
        self.page_content = response.content
        self.soup = BeautifulSoup(self.page_content, 'html.parser')

    def get_all_text(self):
        if self.soup:
            text = self.soup.find_all(string=True)
            stringtext = ""
        for i in text:
            stringtext += "{} ".format(i)
            words = stringtext.split()
        return words
       
scrape = WeatherParser(url)        
words = scrape.get_all_text()

def forecast():
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print('*'*20)
    print("WEATHER FORECAST")
    print('*'*20)
    print('           Day / Night')
    for word in words:
        for j in range(len(week)):
            if word == week[week.index(f'{week[j]}')]:
                print(f'{week[week.index(f'{week[j]}')]}:      ', end=" ")
                for i in range(2,6):
                    print(f'{words[words.index(f'{week[week.index(f'{week[j]}')]}')+i]}', end=" " )
                print()

def forecastGraph():
    plt.title("Погода на цей тиждень, Львів", fontsize=14, color='green', fontweight='bold')
    plt.xlabel("День тижня")
    plt.ylabel("Температура, °C")
    x = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']
    x1 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    y = [int(words[words.index('Mon')+2]), 
        int(words[words.index('Tue')+2]),
        int(words[words.index('Wed')+2]),
        int(words[words.index('Thu')+2]),
        int(words[words.index('Fri')+2]),
        int(words[words.index('Sat')+2]),
        int(words[words.index('Sun')+2])]
    for i in range(len(x)):
        annotation_text = f'{str(y[i])}°C'
        plt.annotate(annotation_text, (x[i], y[i]))

    y1 = [int(words[words.index('Mon')+4]), 
        int(words[words.index('Tue')+4]),
        int(words[words.index('Wed')+4]),
        int(words[words.index('Thu')+4]),
        int(words[words.index('Fri')+4]),
        int(words[words.index('Sat')+4]),
        int(words[words.index('Sun')+4])]
    for i in range(len(x)):
        annotation_text = f'{str(y1[i])}°C'
        plt.annotate(annotation_text, (x[i], y1[i]))

    plt.plot(x,y, "o-", color= 'orange')
    plt.plot(x,y1, "o-", color= (0.3,0.7,1))

    plt.yticks(range(min(y1)-5,max(y)+5))
    plt.grid(axis='x')
    plt.legend(['Вдень', 'Вночі'],
            facecolor= 'white', edgecolor = 'g', shadow=True, fontsize = 8, title = 'Температура',
            loc = 'best')

    filePath = "python_crap/weatherapp/weather.txt"
    file = open(filePath, "w+", encoding="utf-8")
    file.write("Log for weather in Lviv this week\n\n" + '     Day / Night\n')
    for i in range(len(y)):
        file.write(f"{x1[i]}: {y[i]}°C  {y1[i]}°C" + "\n")
    print(f"File with results created at: {filePath}")
    file.close()
    plt.show()