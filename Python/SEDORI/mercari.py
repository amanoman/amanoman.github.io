#%%
pip install chromedriver-binary selenium
#%%
import sys
import time
from selenium import webdriver
import pandas

# %%
# 引数から取得 実行例：python merscraping.py
args = sys.argv
query = args[1]

# %%
# 別途ダウンロードしたchromedriver.exeの場所を指定
#Macの場合chromedriver winの場合chromedriver.exe
browser = webdriver.Chrome(executable_path="chromedriver")
browser.implicitly_wait = 10

url_site = "https://www.mercari.com/jp/".format(query)
browser.get(url_site)

page = 1
item_num = 0
urls = []


# %%
