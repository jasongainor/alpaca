import requests
import json
import pprint #because my consone doesn't display json well
from creds import *

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID' : API_KEY, 'APCA-API-SECRET-KEY' :  SECRET_KEY}
pp = pprint.PrettyPrinter(indent=4)

# Documentation
# https://alpaca.markets/docs/api-documentation/api-v2/


def main():
    selection = input("Select one of the following:\n   1). Make a new order \n   2). See past orders \n   3). Get account info \n")
    if selection == '1':
        makeNewOrder()
    elif selection == '2':
        print('\n Getting past order info:')
        get_orders()
    elif selection == '3':
        print('\n Getting account info:')
        get_account()
    else:
        exit()
    exit()


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    pp.pprint(json.loads(r.content))

def get_orders():
    query = {
        'status': 'all'
        }
    
    r = requests.get(ORDERS_URL, params=query, headers=HEADERS)
    pp.pprint(json.loads(r.content))

def makeNewOrder():
    SYMBOL = input(' ~ What stock symbol do you want to trade? ')
    QTY = input(' ~ How much do you want to trade? ')
    SIDE = input(' ~ Do you want to buy or sell? ')
    TRADE_TYPE = 'market'
    TIME_IN_FORCE = 'day'
    response = create_order(SYMBOL, QTY, SIDE, TRADE_TYPE, TIME_IN_FORCE)

    print(response)

def create_order(symbol, qty, side, trade_type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "filled_qty": "0",
        "type": trade_type,
        "side": side,
        "time_in_force": time_in_force,
        }
    
    r= requests.post(ORDERS_URL, json=data, headers=HEADERS)

    pp.pprint(json.loads(r.content))

if __name__ == "__main__":
    main()