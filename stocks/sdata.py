import requests
import urllib.parse

#given a stock symbol, returns data based off the stock
#data returned is the last known price and the time
#associated with that price
def get_stock_data(symbol):
    #encode stock symbol to be url-safe
    symbol = urllib.parse.quote(symbol)
    #url defined in the IEX API guide for obtaining the
    #latest price for a given stock
    URL='https://api.iextrading.com/1.0/tops/last'
    PARAMS={'symbols' : symbol }
    #making the request to the IEX servers
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    retdata = { 'price' : data[0].get('price'), 'time' : data[0].get('time')}
    return retdata

#function to check if the given stock symbol is valid
#returns true if it is valid, false otherwise
def is_valid_symbol(symbol):
    #encode symbol to be url-safe
    symbol = urllib.parse.quote(symbol)
    URL='https://api.iextrading.com/1.0/tops/last'
    PARAMS={'symbols' : symbol}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    return len(data) > 0
