import logging
import sys


from oanda.oanda import APIClient

import settings



logging.basicConfig(level=logging.INFO,stream=sys.stdout)



if __name__ == "__main__":
    api_client = APIClient(settings.access_token, settings.account_id)
    api_client.get_balance()
