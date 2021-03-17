import requests
from datetime import datetime
from pprint import pprint
import time
import json

chart_sec = 60          # ローソク足の時間軸
file1 = "./FX_BTC_JPY.json"   # 読み込み元のファイル名
file2 = "./FX_BTC_JPY.json"  # 追加保存するファイル名


# Cryptowatchから差分だけを追加して保存する関数
def accumulate_diff_data(min, read_path, save_path, before=0, after=0):
	
	# APIで価格データを取得
	params = {"periods" : min }
	if before != 0:
		params["before"] = before
	if after != 0:
		params["after"] = after
	response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params)
	web_data = response.json()
	web_data_set = set( map( tuple, web_data["result"][str(min)] ))
	
	# ファイルから価格データを取得
	file = open( read_path,"r",encoding="utf-8")
	file_data = json.load(file)
	del file_data["result"][str(min)][-1] # 末尾は被るので削除
	file_data_set = set( map( tuple, file_data["result"][str(min)] ))

	
	# 差分を取得
	diff_data_set = web_data_set - file_data_set
	diff_data = list(diff_data_set)
		
	# 差分を追加する
	if len(diff_data) != 0:
		print("{}件の追加データがありました".format( len(diff_data) ))
		diff_data.sort( key=lambda x:x[0] )
		file_data["result"][str(min)].extend( diff_data )
		pprint(diff_data)
	
	#ファイルに書き込む
	file = open( save_path,"w",encoding="utf-8")
	json.dump(file_data,file)
	
	return file_data

# ---- ここからメイン ----

# 差分の価格データを保存する
accumulate_diff_data(chart_sec, file1, file2)