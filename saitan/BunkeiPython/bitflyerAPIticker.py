import requests
response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400&after=1516147200")
response_0115 = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400&after=1515974400")

data = response.json()
data_0115 = response_0115.json()

data_lists = data["result"]["86400"]
data_lists_0115 = data_0115["result"]["86400"]

for data_list_0115 in data_lists_0115:
    if data_list_0115[0] == 1515974400:
        print(f"前終値{data_list_0115[4]}")
for data_list in data_lists:
    if data_list[0] == 1516147200: 
        print(f"始  値{data_list[1]}")
        print(f"最高値{data_list[2]}")
        print(f"最安値{data_list[3]}")
        print(f"終  値{data_list[4]}")



#print(datas["result"]["86400"][-1])