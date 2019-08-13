from stocks.models import Portfolio, Transactions, Profile
from stocks.sdata import get_stock_data

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
    update_user_cash(user, True, num_of_shares * price)
            
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
    user = request.user
    p = Profile.objects.filter(user=user)
    cash = p[0].current_cash
    
    stock_ticker = form.cleaned_data['stock_ticker'].upper()
    quantity = form.cleaned_data['num_of_shares']
    net_price = get_stock_data(stock_ticker).get('price') * quantity
    
    return cash > net_price

#function to change the user's current cash 
def update_user_cash(user, bought, net_price):
    p = Profile.objects.filter(user=user)
    user_profile = p[0]
    if bought:
        user_profile.current_cash -= net_price
    else:
        user_profile.current_cash += net_price
    user_profile.save()

#function to return all items in a users portfolio
def get_portfolio(user):
    p = Portfolio.objects.filter(user=user)
    retval = []
    for user_stock in p:
        retval.append({ 'symbol' : user_stock.stock_ticker,
                        'shares' : user_stock.num_of_shares,
                        'worth' : user_stock.price_bought,
                        })
           
