# pyTradingBot
Trading bots with Python

# tradingBotArchitecture:
Algorithmic traders may be interested in developing more sophisticated trading bots that incorporate functions such as multiple data analyses, news sentiment analysis, and artificial intelligence.
In order to manage the increased complexity of the bot, it is crucial to have a clean, well-structured software architecture.

The purpose of this repo is to propose a generic architecture for trading bots that can be applied to any type of market. An object-oriented, typed data model is implemented in Python as part of the architecture.

Among the components/classes of the model are:

- Data Loader
- Bot
- Logging System
- Order
- Trade
- Position
- Broker

# visualizingTradingSignals:
We want to determine when would be a good time to buy or sell our stock or cryptocurrency, but how can we do this? One way is to use moving averages to determine the direction of a market.
A Simple Moving Avergage (SMA) is when we take an average of the last n closing prices of historical trading data. If we are looking at the daily chart, each candlestick or data point will be 1 day. The SMA50 will be an average of the last 50 days of closing prices. This alone does not do much for us, aside from smoothing out the “noise” in a market. Where this gets interesting is when you compare it with another moving average, for example SMA200. Every time the SMA50 crosses above the SMA200 we know that the market is in an upward trend, and when the SMA50 crosses below the SMA200 it is a downward trend. You can use any moving averages you like but this combination is considered special. When the SMA50 crosses above the SMA200 it’s known as the “Golden Cross”, and when the SMA50 crosses below the SMA200 it is known as the “Death Cross”. When this event occurs it usually is followed by a strong price movement.

# easyBot:
Easy bot for trading

# sentAlgo:
Sentiment analysis algorithms types

