import requests
import json
from pprint import pprint

# 現在の天気を取得する：神戸
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="取得したAPIキー")

jsondata = requests.get(url).json()
pprint(jsondata)
