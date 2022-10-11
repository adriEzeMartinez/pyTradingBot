#  Main
if __name__ == '__main__':
    #  Create new bot
    config = Config(symbols=['litecoin', 'ethereum'], cash_per_trade=100, total_cash=10000, data_fetch_interval=60)
    bot = Bot(config)
    bot.start()