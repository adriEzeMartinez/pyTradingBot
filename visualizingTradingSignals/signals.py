import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta

resp = requests.get("https://eodhistoricaldata.com/api/eod/AAPL?api_token=demo&fmt=json")
json_data = json.loads(resp.content)
df = pd.DataFrame(json_data)
df

df["sma50"] = df.close.rolling(50, min_periods=50).mean()
df["sma200"] = df.close.rolling(200, min_periods=200).mean()
df

df.dropna(inplace=True)
df

plt.figure(figsize=(30,10))
plt.plot(df["close"], color="black", label="Price")
plt.plot(df["sma50"], color="blue", label="SMA50")
plt.plot(df["sma200"], color="green", label="SMA200")
plt.ylabel("Price")
plt.xticks(rotation=90)
plt.title("APPL Daily SMA50/SMA200")
plt.legend()
plt.show()

df = df.tail(365)

df.set_index(['date'], inplace=True)
df

plt.figure(figsize=(30,10))
plt.plot(df["close"], color="black", label="Price")
plt.plot(df["sma50"], color="blue", label="SMA50")
plt.plot(df["sma200"], color="green", label="SMA200")
plt.ylabel("Price")
plt.xticks(rotation=90)
plt.title("APPL Daily SMA50/SMA200")
ax = plt.gca()
for index, label in enumerate(ax.xaxis.get_ticklabels()):
  if index % 7 != 0:
    label.set_visible(False)
plt.legend()
plt.show()

pd.options.mode.chained_assignment = None
df.loc[df["sma50"] > df["sma200"], "sma50gtsma200"] = True
df["sma50gtsma200"].fillna(False, inplace=True)
df.loc[df["sma50"] < df["sma200"], "sma50ltsma200"] = True
df["sma50ltsma200"].fillna(False, inplace=True)
df

df["sma50gtsma200co"] = df.sma50gtsma200.ne(df.sma50gtsma200.shift())
df.loc[df["sma50gtsma200"] == False, "sma50gtsma200co"] = False
df["sma50ltsma200co"] = df.sma50ltsma200.ne(df.sma50ltsma200.shift())
df.loc[df["sma50ltsma200"] == False, "sma50ltsma200co"] = False
df

buysignals = df[df["sma50gtsma200co"] == True]
buysignals

sellsignals = df[df["sma50ltsma200co"] == True]
sellsignals

for idx in buysignals.index.tolist():
  plt.plot(
      idx,
      df.loc[idx]["close"],
      "g*",
      markersize=25
  )
for idx in sellsignals.index.tolist():
  plt.plot(
      idx,
      df.loc[idx]["close"],
      "r*",
      markersize=25
  )


plt.figure(figsize=(30,10))
plt.plot(df["close"], color="black", label="Price")
plt.plot(df["sma50"], color="blue", label="SMA50")
plt.plot(df["sma200"], color="green", label="SMA200")
plt.ylabel("Price")
plt.xticks(rotation=90)
plt.title("APPL Daily SMA50/SMA200")
for idx in buysignals.index.tolist():
  plt.plot(
      idx,
      df.loc[idx]["close"],
      "g*",
      markersize=25
  )
for idx in sellsignals.index.tolist():
  plt.plot(
      idx,
      df.loc[idx]["close"],
      "r*",
      markersize=25
  )
ax = plt.gca()
for index, label in enumerate(ax.xaxis.get_ticklabels()):
  if index % 7 != 0:
    label.set_visible(False)
plt.legend()
plt.show()

df["ema12"] = df["close"].ewm(span=12, adjust=False).mean()
df["ema26"] = df["close"].ewm(span=26, adjust=False).mean()
df["macd"] = df["ema12"] - df["ema26"]        
df["signal"] = df["macd"].ewm(span=9, adjust=False).mean()
df.loc[df["macd"] > df["signal"], "macdgtsignal"] = True
df["macdgtsignal"].fillna(False, inplace=True)
df.loc[df["macd"] < df["signal"], "macdltsignal"] = True
df["macdltsignal"].fillna(False, inplace=True)
df

buysignals = df[(df["sma50gtsma200co"] == 1) & (df["macdgtsignal"] == 1)]
sellsignals = df[(df["sma50ltsma200co"] == 1) & (df["macdltsignal"] == 1)]

df["macdgtsignalco"] = df.macdgtsignal.ne(df.macdgtsignal.shift())
df.loc[df["macdgtsignal"] == False, "macdgtsignalco"] = False
df["macdltsignalco"] = df.macdltsignal.ne(df.macdltsignal.shift())
df.loc[df["macdltsignal"] == False, "macdltsignalco"] = False
buysignals = df[(df["sma50gtsma200co"] == 1) & (df["macdgtsignal"] == 1)]
sellsignals = df[(df["sma50gtsma200"] == 1) & (df["macdltsignalco"] == 1)]

df["rsi14"] = ta.rsi(df["close"], length=14, fillna=50)

