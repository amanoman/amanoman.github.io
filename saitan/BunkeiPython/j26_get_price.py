import websocket
import colorlog
import json
import logging
import logging.handlers
import sys
import os
import datetime
import argparse
import multiprocessing


URL = 'wss://ws.lightstream.bitflyer.com/json-rpc'

CHANNELS = [
   '{}_{}'.format(channel, product)
   for channel in [
       'lightning_board_snapshot',
       'lightning_board',
       'lightning_ticker',
       'lightning_executions',
   ]
   for product in [
       'BTC_JPY',
       'FX_BTC_JPY',
   ]
]


class App:

   def __init__(self, out_root_dir, channel):
       self.channel = channel
       self.out_dir = os.path.join(out_root_dir, channel)
       self.logger = logging.getLogger('{}.{}'.format(__name__, self.channel))

       self.out_file = None
       self.out_file_date = None

   def run_forever(self):
       self.setup_logger()

       # websocket-clientはinspect.ismethodでコールバックの型を認識して処理を変えてくる。
       # （かなり軽率な仕様だと思うのでやめてほしい……）
       # bound methodだと何故かwsを貰えないので、lambdaでごまかす。
       ws = websocket.WebSocketApp(
           URL,
           header=None,
           on_open=lambda w: self.on_open(w),
           on_message=lambda w, m: self.on_message(w, m),
           on_error=lambda w, e: self.on_error(w, e),
           on_close=lambda w: self.on_close(w),
       )
       ws.run_forever()

   def setup_logger(self):
       log_path = os.path.join(self.out_dir, 'log', 'log.txt')
       os.makedirs(os.path.dirname(log_path), exist_ok=True)

       stderr_handler = colorlog.StreamHandler()
       stderr_handler.setFormatter(colorlog.ColoredFormatter(
           '%(log_color)s[%(asctime)s %(levelname)s:%(name)s] %(message)s'))

       file_handler = logging.handlers.TimedRotatingFileHandler(
           filename=log_path, when='MIDNIGHT')

       logging.basicConfig(level=logging.INFO, handlers=[
                           stderr_handler, file_handler])

   def check_reopen_out_file(self):
       today = datetime.date.today()
       if self.out_file_date == today:
           return

       if self.out_file:
           self.out_file.close()

       out_file_path = os.path.join(
           self.out_dir, 'stream', '{}.txt'.format(today.isoformat()))
       os.makedirs(os.path.dirname(out_file_path), exist_ok=True)

       self.out_file = open(out_file_path, 'w')
       self.out_file_date = today
       self.logger.info('Writing to: {}'.format(out_file_path))

   def on_open(self, ws):
       self.logger.info('open')
       msg = {
           'method': 'subscribe',
           'params': {
               'channel': self.channel
           }
       }
       ws.send(json.dumps(msg))

   def on_message(self, ws, message):
       body = json.loads(message)['params']['message']
       self.check_reopen_out_file()
       self.out_file.write(json.dumps(body))
       self.out_file.write('\n')

   def on_close(self, ws):
       self.logger.warning('closed')

   def on_error(self, ws, error):
       self.logger.exception(error)
       if isinstance(error, KeyboardInterrupt):
           sys.exit(1)


def subprocess_main(out_dir, channel):
   while True:
       try:
           app = App(out_dir, channel)
           app.run_forever()
       except Exception as e:
           logger = logging.getLogger('{}.{}'.format(__name__, channel))
           logger.exception(e)


def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('--out-dir', required=True)
   args = parser.parse_args()

   processes = []
   for channel in CHANNELS:
       p = multiprocessing.Process(
           target=subprocess_main, args=(args.out_dir, channel))
       p.daemon = True
       p.start()
       processes.append(p)

   for p in processes:
       p.join()


if __name__ == '__main__':
   main()