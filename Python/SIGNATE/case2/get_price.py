import requests
response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400&after=1514764800")
data = response.json()

#print(data)
for item in data["result"]["86400"]:
    if item[0]==1516147200:
        print(item[3])

