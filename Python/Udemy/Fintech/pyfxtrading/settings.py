import configparser



conf = configparser.ConfigParser()
conf.read('settings.ini')

accunt_id = conf['oanda']['acount_id']
access_token = conf['oanda'][access_token]

