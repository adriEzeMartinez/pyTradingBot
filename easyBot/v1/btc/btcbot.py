import requests, json as j, pandas as pd, time
#https://min-api.cryptocompare.com/
token = "dd52abb3c8036693290b36e87929412c5b0161d84ec012d7140e72147be4d29b"

# Trae los datos desde cryptocompare
def getData(s,token):        
    url = "https://min-api.cryptocompare.com/data/v2/histominute?fsym="+s
    url += "&tsym=USD&limit=100&e=bitstamp&token="+token    
    json = j.loads(requests.get(url = url).text)
    df = pd.DataFrame(json['Data']['Data']).dropna()
    return df

# medias moviles
def sma(serie,ruedas,nombreColumna):
    rta=pd.DataFrame({nombreColumna:[]})
    i = 0
    for valor in serie:
        if(i >= ruedas):
            promedio = sum(serie[i-ruedas+1:i+1])/ruedas
            rta.loc[i] = promedio
        i = i+1
    return rta

def getTabla(simbolo,nRapida,nLenta,token):    
    data = getData(simbolo,token)
    rapidas = sma(data['close'],nRapida,"rapida")
    lentas = sma(data['close'],nLenta,"lenta")
    tabla = rapidas.join(lentas).join(data['close']).dropna().reset_index()
    return tabla

# decide si comprar o vender o mantenerse en espera ya sea comprado o vendido,
def accion(cruce, pos, precio):
    if(cruce>1):
        if (pos=="Wait"):
            print("--Buy Order $"+str(precio)+"--")
        pos = "hold"
    else:
        if (pos=="hold"):
            print("--Sell Order $"+str(precio)+"--")
        pos = "Wait"       
    return pos


datos = getData("BTC",token)
print(datos)

precios = getData("BTC",token)
smas20 = sma(precios['close'],20,'SMA_20')
print(smas20)

tabla = getTabla("BTC",10,20,token)
print(tabla)

pos = "Wait"
while True:
    tabla = getTabla("BTC",10,20,token)
    cruce = tabla['rapida'].iloc[-1] / tabla['lenta'].iloc[-1]
    precio = tabla['close'].iloc[-1]
    pos = accion(cruce, pos, precio)
    print(pos+" $" +str(precio) )
    time.sleep(60)

