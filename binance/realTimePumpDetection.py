import time
from binance.client import Client

api_key = "some_key"
api_secret = "some_secret"

client = Client(api_key, api_secret)


def get_trading_symbols(limit):
    list = []
    tickers = client.get_ticker()

    for i in range(len(tickers)):
        tickers[i]['quoteVolume'] = float(tickers[i]['quoteVolume'])

    tickers = sorted(tickers, key=lambda x: x['quoteVolume'], reverse=True)
    for item in tickers:
        symbolpair = item['symbol']

        if float(item['quoteVolume']) > 50000:
            list.append(symbolpair)

    symbols = list[:limit]
    return symbols

top_coins_movers = []
top_movers = {}

def get_movers(qty, move):
    global top_coins_movers
    global top_movers

    a = get_trading_symbols(qty)
    time.sleep(5)
    new_a = get_trading_symbols(qty)

    change_previous = [(a[i], i) for i in range(len(a)) if a[i] != new_a[i]]
    change_new = [(new_a[i], i) for i in range(len(new_a)) if new_a[i] != a[i]]

    for item_new in change_new:
        item_new = list(item_new)
        for item_old in change_previous:
            item_old = list(item_old)
            if item_new[0] == item_old[0]:
                if item_new[0] not in top_movers:
                    top_movers[item_new[0]] = item_old[1] - item_new[1]
                else:
                    top_movers[item_new[0]] = top_movers[item_new[0]] + (item_old[1] - item_new[1])

    top_movers_filtered = {}
    for item in top_movers:
        if top_movers[item] > move:
            top_movers_filtered[item] = top_movers[item]
    top_movers_filtered_sorted = dict(sorted(top_movers_filtered.items(), key=lambda item: item[1]))

    top_movers_filtered_sorted = dict(reversed(list(top_movers_filtered_sorted.items())))


    return top_movers_filtered_sorted

price_baseline ={}
top_coins_movers = []
top_movers = {}

while True:
    top_movers = get_movers(300, 3)
    if top_movers:
        for top_mover in top_movers:
            AvgPrice = float(client.get_ticker(symbol=top_mover)['weightedAvgPrice'])

            if top_mover not in price_baseline:
                price_baseline[top_mover] = AvgPrice

            if AvgPrice > price_baseline[top_mover] * 1.02:
                print(f'Trading pair: {top_mover}, Price: {AvgPrice}, Price baseline: {price_baseline[top_mover]}, Rank: {top_movers[top_mover]}')