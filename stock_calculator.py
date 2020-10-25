import json
import requests
import os


class StockCalculator:
    def __init__(self, stock):
        self.stock = stock
        self.finviz = "https://finnhub.io/api/v1"
        self.api_key = os.environ['API_KEY']

    def find_competition(self):
        response = requests.get("{}/stock/peers?symbol={}&token={}".format(self.finviz, self.stock, self.api_key))
        print(response.json())

test = StockCalculator('AAPL')
test.find_competition()




