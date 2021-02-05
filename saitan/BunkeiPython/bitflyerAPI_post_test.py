import hashlib
import hmac
import requests
import datetime
import json

api_key = ""
api_secret = ""

base_url = "https://api.bitflyer.jp"
path_url = "/v1/me/sendchildorder"
method ="POST"

timestamp = str(datetime.datetime.today()) #文字に変換しないとhttps通信で送れない

#bitFlyerAPIで必要になるパラメーター
param = {
    "product_code" : "FX_BTC_JPY",
    "child_order_type" : "LIMIT",
    "side" : "BUY",
    "price" : 3050000,
    "size" : 0.01,
}
body = json.dumps(param) #json.dumpu()でjson形式に変換

#認証のための暗号文（署名)の作成
message = timestamp + method + path_url + body
signature = hmac.new(bytearray(api_secret.encode('utf-8')), message.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

#通信データのヘッダー作成
headers = {
	'ACCESS-KEY' : api_key,
	'ACCESS-TIMESTAMP' : timestamp,
	'ACCESS-SIGN' : signature,
	'Content-Type' : 'application/json'
}

#APIリクエストを送る
response = requests.post(base_url + path_url, data = body, headers = headers)
print(response.status_code)
print(response.json())