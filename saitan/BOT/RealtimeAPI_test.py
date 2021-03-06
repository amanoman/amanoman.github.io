#https://note.com/kunmosky1/n/n2a0085d71426 くもすけさんのnote参照

#!/usr/bin/python3
import json
import websocket
import hmac
from hashlib import sha256
from secrets import token_hex
import time
from threading import Thread
import signal
import os
from PASSWORDS.password import *

# -------------------------------------
key = bitFlyer_apiKey
secret = bitFlyer_secret

end_point = 'wss://ws.lightstream.bitflyer.com/json-rpc'

public_channels = ['lightning_executions_FX_BTC_JPY',
                  'lightning_board_snapshot_FX_BTC_JPY']
private_channels = ['child_order_events', 'parent_order_events']
# -------------------------------------


def quit_loop(signal, frame):
   os._exit(0)


class bFwebsocket(object):
   def __init__(self, end_point, public_channels, private_channels, key, secret):
       self._end_point = end_point
       self._public_channels = public_channels
       self._private_channels = private_channels
       self._key = key
       self._secret = secret
       self._JSONRPC_ID_AUTH = 1

   def startWebsocket(self):
       def on_open(self):
           print("Websocket connected")

           if len(self._private_channels) > 0:
               auth(ws)

           if len(self._public_channels) > 0:
               params = [{'method': 'subscribe', 'params': {'channel': c}}
                         for c in self._public_channels]
               self.ws.send(json.dumps(params))

       def on_error(self, error):
           print(error)

       def on_close(self):
           print("Websocket closed")

       def run(ws):
           while True:
               ws.run_forever()
               time.sleep(3)

       def on_message(self, message):
           messages = json.loads(message)

           # auth レスポンスの処理
           if 'id' in messages and messages['id'] == self._JSONRPC_ID_AUTH:
               if 'error' in messages:
                   print('auth error: {}'.format(messages["error"]))
               elif 'result' in messages and messages['result'] == True:
                   params = [{'method': 'subscribe', 'params': {'channel': c}}
                             for c in self._private_channels]
                   self.ws.send(json.dumps(params))

           if 'method' not in messages or messages['method'] != 'channelMessage':
               return

           params = messages["params"]
           channel = params["channel"]
           recept_data = params["message"]

           if channel == 'child_order_events':
               for r in recept_data:
                   print(r['event_date'], r['child_order_acceptance_id'],
                         r['event_type'], r['side'], r['price'], r['size'])
           else:
               print(channel, len(recept_data))

       def auth(self):
           now = int(time.time())
           nonce = token_hex(16)
           sign = hmac.new(self._secret.encode(
               'utf-8'), ''.join([str(now), nonce]).encode('utf-8'), sha256).hexdigest()
           params = {'method': 'auth', 'params': {'api_key': self._key, 'timestamp': now,'nonce': nonce, 'signature': sign}, 'id': self._JSONRPC_ID_AUTH}
           self.ws.send(json.dumps(params))

       ws = websocket.WebSocketApp(self._end_point, on_open=on_open,on_message=on_message, on_error=on_error, on_close=on_close)
       websocketThread = Thread(target=run, args=(ws, ))
       websocketThread.start()


if __name__ == '__main__':
   # Ctrl+Cが押された時の処理
   signal.signal(signal.SIGINT, quit_loop)

   ws = bFwebsocket(end_point, public_channels, private_channels, key, secret)
   ws.startWebsocket()

   while True:
       time.sleep(1)



test_api = bFwebsocket()
test_api.startWebsocket()#.on_close()