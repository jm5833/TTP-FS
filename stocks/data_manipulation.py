import stocks.stock_data
from stocks.models import Portfolio, Transactions
from stocks.stock_data import get_stock_data

#function to add a transaction to the 
#transactions database
def save_transaction(request, form):
    stock_ticker = form.cleaned_data['stock_ticker']
    #retrieve the data from the submitted form
    post = form.save(commit=False)
    post.user = request.user
    post.price = get_stock_data(stock_ticker).get('price')
    post.bought = True
    post.save()

#function to add a stock to the portfolio table
def update_portfolio(request, form):
    user = request.user
    stock_ticker = form.cleaned_data['stock_ticker']
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
            
#function to add an entry into the portfolio table
def add_portfolio(user, stock_ticker, num_of_shares, price):
    p = Portfolio(
                    user=user, 
                    stock_ticker=stock_ticker, 
                    num_of_shares=num_of_shares,
                    price_bought=price,
                    )
    p.save()
