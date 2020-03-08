#%%
import requests
from bs4 import BeautifulSoup

load_url = "https://www.mercari.com/jp/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup)

＃メルカリはスクレイピング禁止のためrequetsではサーバで弾かれて403エラー