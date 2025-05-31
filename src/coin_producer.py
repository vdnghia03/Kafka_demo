import time
from quixstreams import Application
from constants import COINMARKET_API

from requests import Session, Timeout, TooManyRedirects
import json
from pprint import pprint

app = Application(
    broker_address="localhost:9092",
    consumer_group="coin_group",
)

coins_topic = app.topic(name="coins", value_serializer="json")


def get_latest_coin_data(symbol="BTC"):
    api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COINMARKET_API,
    }

    parameters = {
        "symbol": symbol,
        "convert": "USD",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(api_url, params=parameters)
        return json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

if __name__ == "__main__":
    result = get_latest_coin_data()
    pprint(result)


