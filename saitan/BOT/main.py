# coding: utf-8
import socketio
from secrets import token_hex
from hashlib import sha256
import hmac
import time
import signal
import os
from PASSWORDS.password import *

# -------------------------------------
key = bitFlyer_apiKey
secret = bitFlyer_secret
# -------------------------------------


class bFwebsocket(object):
   def __init__(self, end_point, key, secret):
       self._connected = False
       self._auth_completed = False
       self._end_point = end_point
       self._key = key
       self._secret = secret

       self._sio = socketio.Client()
       self._sio.on('connect', self.on_connect)
       self._sio.connect(self._end_point, transports=['websocket'])
       while not self._connected:
           time.sleep(1)

   def on_connect(self):
       print('SocketIO connected')
       self._connected = True

   def start_auth(self):
       now = int(time.time())
       nonce = token_hex(16)
       sign = hmac.new(self._secret.encode('utf-8'),
                       ''.join([str(now), nonce]).encode('utf-8'),
                       sha256).hexdigest()
       params = {'api_key': self._key, 'timestamp': now,
                 'nonce': nonce, 'signature': sign}
       self._sio.emit('auth', params, callback=self.on_auth)
       print('Auth process started')
       while not self._auth_completed:
           time.sleep(1)

   def on_auth(self, recept_data):
       print('Auth process done')
       self._auth_completed = True

   def regist_handler(self, channel, handler):
       self._sio.on(channel, handler)
       self._sio.emit('subscribe', channel)


def quit_loop(signal, frame):
   os._exit(0)


if __name__ == '__main__':
   # Ctrl+Cが押された時の処理
   signal.signal(signal.SIGINT, quit_loop)

   def on_executions(recept_data):
       print('lightning_executions_FX_BTC_JPY')
       print(recept_data)

   def on_child_order_events(recept_data):
       print('child_order_events')
       print(recept_data)

   ws = bFwebsocket('https://io.lightstream.bitflyer.com', key, secret)
   ws.start_auth()

   ws.regist_handler(
       channel='lightning_executions_FX_BTC_JPY',
       handler=on_executions)

   ws.regist_handler(
       channel='child_order_events',
       handler=on_child_order_events)

   while True:
       time.sleep(1)