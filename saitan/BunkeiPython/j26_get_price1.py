import websocket
import colorlog
import json
import logging
import sys

logger = logging.getLogger(__name__)

def save_price():
    #ファイルに書き込む
    file = open("./{0}-{1}-price.json".format(price[0]["close_time"],price[-1]["close_time"]),"w",encoding="utf-8")
    json.dump(price,file,indent=4)


def main():
   handler = colorlog.StreamHandler()
   handler.setFormatter(colorlog.ColoredFormatter(
       '%(log_color)s[%(levelname)s:%(name)s] %(message)s'))
   logging.basicConfig(level=logging.INFO, handlers=[handler])

   url = 'wss://ws.lightstream.bitflyer.com/json-rpc'
   channel = 'lightning_ticker_BTC_JPY'

   def on_open(ws):
       logger.info('open')
       ws.send(json.dumps(
               {
                   'method': 'subscribe',
                   'params': {'channel': channel}
               }
       ))

   def on_message(ws, message):
       body = json.loads(message)['params']['message']
       print(body)

   def on_close(ws):
       logger.info('closed')

   def on_error(ws, error):
       logger.exception(error)
       if isinstance(error, KeyboardInterrupt):
           sys.exit(1)

   # ネットワークが切れたりするとon_error, on_closeあたりが呼ばれて帰ってきちゃうので、ループで囲う
   # websocketが食べちゃうからExceptionは外まで出てこないっぽいんだけど、一応こっちでもキャッチするコード入れとく
   while True:
       try:
           websocket.enableTrace(True)
           ws = websocket.WebSocketApp(
               url,
               on_open=on_open,
               on_message=on_message,
               on_error=on_error,
               on_close=on_close,
           )
           ws.run_forever()
       except Exception as e:
           logger.exception(e)


if __name__ == '__main__':
    main()
