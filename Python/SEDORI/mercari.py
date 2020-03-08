#%%
pip install selenium

# %%
import sys
import time
from selenium import webdriver

# %%
args = sys.argv
query = args[1]

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.implicitly_wait = 10

# %%
