import requests
import json
from pprint import pprint

# 5日間（3時間ごと）の天気を取得する：東京
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="取得したAPIキー")

jsondata = requests.get(url).json()
pprint(jsondata)
