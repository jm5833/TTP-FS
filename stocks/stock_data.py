import requests

#given a stock symbol, returns data based off the stock
#data returned is the last known price and the time
#associated with that price
def get_stock_data(symbol):
    #url defined in the IEX API guide for obtaining the
    #latest price for a given stock
    URL='https://api.iextrading.com/1.0/tops/last'
    PARAMS={'symbols' : symbol }
    #making the request to the IEX servers
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    retdata = { 'price' : data[0].get('price'), 'time' : data[0].get('time')}
    return retdata

