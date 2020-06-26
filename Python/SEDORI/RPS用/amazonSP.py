from selenium import webdriver
from selenium.webdriver.common.keys import keys
import re
import time
import sys
import datatime
import pandas as pd 

names = []
browser = webdriver.Chrome(executable_path="chromedriver.exe")

url_site ="https://www.amazon.co.jp/s?me=A3T97Q67P7MVHW&marketplaceID=A1VC38T7YXB528"
browser.get(url_site)
time.sleep(5)

browser.close()
 


