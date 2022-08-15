import requests
from bs4 import BeautifulSoup
import time



class Weather:
    WEATHER_MOSCOW = 'https://www.google.com/search?q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}

    current_temper = 20
    dif = 5

    def __init__(self):
        self.current_temp = float(self.get_temp().replace(",","."))

    def get_temp(self):
        full_page = requests.get(self.WEATHER_MOSCOW, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "wob_t q8U8x"})
        return convert[0].text

    def check_weather(self):
        temp = float(self.get_temp().replace(",","."))
        if temp >= self.current_temp + self.dif:
            print("Становится жарко!")
        elif temp <= self.current_temp - self.dif:
            print("Становится холоднее!")
        print('Температура в Москве: ' + str(temp))
        time.sleep(3)
        self.check_weather()

temp = Weather()
temp.check_weather()
