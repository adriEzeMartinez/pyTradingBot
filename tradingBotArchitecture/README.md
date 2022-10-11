#  Backtesting.py:

Python backtesting framework, used in the architecture proposed in this folder. Since it has an object-oriented, typed data model, it is also compatible with bot software architectures.

backtesting.py, a Python backtesting framework, is used in the architecture proposed in this post. Since it has an object-oriented, typed data model, it is also compatible with bot software architectures.

To be used by the bot, I defined the following enums for Position, Side, and Order Status in htyueo.py file

All configuration parameters for the Bot are contained in the Config class (config.py). In this section, you can specify which symbols to trade, how much cash is available for trading, or how often to retrieve new price information.

Using the Bot class (bot.py), you can set up logging, fetch data regularly, or run a strategy. This class owns all the secondary classes.

Logging (utioe.py) is currently performed using the Python library loguru, but can be replaced with other logging frameworks if desired.

The Bot sets up the logging system during initialization, which other classes can then use.

Either your exchange or data API can be used to fetch data using the Data Loader class.

I’m grabbing OHLC crypto data from CoinGecko.com in this example, but you might want to modify it to get other types of data (pricedataloader.py).

A symbol, position, size, limit, stop and limit loss are stored in the Order class when placing an order on an exchange (order.py). 

We create trades after an entry order has been executed by the exchange and the order status has been confirmed.

Exit orders are closed when the exchange confirms the status and we look up the last matching trade based on symbol, size, and position.

The broker keeps a list of closed trades called ‘closed_trades’.

Additionally, I’m passing the Price Loader into this trade to calculate the profit/loss of any open trade (trade.py)

All open trades are grouped by symbol in the Position class, which identifies all held positions.

With the help of the broker, this class calculates the position size and P&L dynamically. (ytueh12.py)

An order list, trade list, position list, and closed trade list are maintained by the Broker.

Positions could also be maintained here. The exchange may, however, be a more accurate source.

Brokers perform two main functions. ‘submit_order()’ submits buy/sell orders to the exchange for long and short positions.

To close an order, we look up its size in the list of open trades.

At regular intervals, we check the order status with the exchange in the ‘check_order_status()’ function. A trade is opened if the entry order has been filled, or it is closed if the exit order has been filled.

In addition to increasing and decreasing the available cash amount, we also keep track of the funds we have for investment. As an alternative, we could get this amount from the exchange.

Here, you will need to implement API integration with your exchange (tradingbot1.py)

The main() function instantiates and configures the Bot, then calls start() to start the loop to pull prices and execute the strategy (tradingbot2.py)