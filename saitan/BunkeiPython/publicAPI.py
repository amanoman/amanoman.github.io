import requests
response = requests.get("https://api.bitflyer.jp/v1/ticker/")
r_data = response.json()

board = requests.get("https://api.bitflyer.jp/vi/board/")
b_data = board.json()

executions = requests.get("https://api.bitflyer.jp/vi/executions/")
e_data = executions.json()

health = requests.get("https://api.bitflyer.jp/vi/gethealth/")
h_data = health.json()

print(r_data)
print(f"【買い気配値】{r_data['best_bid_size']}")

print(b_data)
print(e_data)
print(h_data)