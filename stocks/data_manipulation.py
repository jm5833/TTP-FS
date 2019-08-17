from stocks.models import Transactions, Portfolio
from users.models import User
from stocks.sdata import get_stock_data
from decimal import Decimal

#function to add a transaction to the 
#transactions database
def save_transaction(request, form):
    stock_ticker = form.cleaned_data['stock_ticker'].upper()
    #retrieve the data from the submitted form
    post = form.save(commit=False)
    post.user = request.user
    post.price = get_stock_data(stock_ticker).get('price')
    post.bought = True
    post.save()

#function to add a stock to the portfolio table
def update_portfolio(request, form):
    user = request.user
    stock_ticker = form.cleaned_data['stock_ticker'].upper()
    num_of_shares = form.cleaned_data['num_of_shares']
    price = get_stock_data(stock_ticker).get('price')
    #retrieve the number of stocks owned by the user for s_ticker
    user_stock = Portfolio.objects.filter(user=user, stock_ticker=stock_ticker)
    #if the user has no stocks in that company, add it to their portfolio
    if len(user_stock) == 0:
        add_portfolio(user, stock_ticker, num_of_shares, price)
    #compound stock quantity if the user already owns stock in said company
    else:
        p = user_stock[0]
        p.num_of_shares += num_of_shares
        p.save()
    update_user_cash(user.pk, True, num_of_shares * price)
            
#function to add an entry into the portfolio table
def add_portfolio(user, stock_ticker, num_of_shares, price):
    p = Portfolio(
                    user=user, 
                    stock_ticker=stock_ticker, 
                    num_of_shares=num_of_shares,
                    price_bought=price,
                    )
    p.save()

#function to check if the user has enough money to purchase stock
#returns True if the user has enough cash
#returns False if they don't have enough cash
def balance_check(request, form):
    cash = get_current_cash(request.user.pk)
    stock_ticker = form.cleaned_data['stock_ticker'].upper()
    quantity = form.cleaned_data['num_of_shares']
    net_price = get_stock_data(stock_ticker).get('price') * quantity
    
    return cash > net_price

#function to change the user's current cash 
def update_user_cash(user_pk, bought, net_price):
    u = User.objects.filter(pk=user_pk)
    user = u[0]
    if bought:
        user.current_cash -= net_price
    else:
        user.current_cash += net_price
    user.save()

#function to return all items in a users portfolio
def get_portfolio(user):
    p = Portfolio.objects.filter(user=user)
    retval = []
    for user_stock in p:
        stock_ticker = user_stock.stock_ticker
        num_of_shares = user_stock.num_of_shares
        worth = user_stock.price_bought
        
        current_price = get_stock_data(stock_ticker).get('price')
        color = ''
        if worth > current_price:
            color = 'red'
        elif worth < current_price:
            color = 'green'
        else:
            color = 'grey'
        retval.append({ 'symbol' : stock_ticker,
                        'shares' : num_of_shares,
                        'current_price' : current_price,
                        'color' : color
                        })
    return retval

#function that takes in a user and returns the net worth of their portfolio
def get_portfolio_net(user):
    profile_net = float(0)
    u = User.objects.filter(pk=user.pk)
    profile_net += float(u[0].current_cash)

    p = Portfolio.objects.filter(user=user)
    for stock in p:
        stock_ticker = stock.stock_ticker
        shares = stock.num_of_shares
        current_price = get_stock_data(stock_ticker).get('price')
        profile_net += (current_price * shares)
    return round(profile_net, 2)

#function to return a list of all transactions the 
#given user has made
def get_transactions(user):
    t = Transactions.objects.filter(user=user)
    user_transactions = []
    for ut in t:
        symbol = ut.stock_ticker.upper()
        shares = ut.num_of_shares
        bought = 'Bought' if ut.bought else 'Sold'
        price = ut.price
        date = ut.date
        user_transactions.append({'symbol' : symbol,
                                  'shares' : shares,
                                  'bought' : bought,
                                  'price' : price,
                                  'date' : date,
                                })
    return user_transactions

#function to return a user's current balance
def get_current_cash(user_pk):
    return User.objects.filter(pk=user_pk)[0].current_cash
