import stocks.stock_data
import stocks.models
from stocks.stock_data import get_stock_data

#function to add a transaction to the 
#transactions database
def save_post(request, form):
    s_ticker = form.cleaned_data['stock_ticker']
    #retrieve the data from the submitted form
    post = form.save(commit=False)
    post.user = request.user
    post.price = get_stock_data(s_ticker).get('price')
    post.bought = True
    post.save()
