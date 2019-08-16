from django import forms
from stocks.models import Portfolio, Transactions
from stocks.sdata import is_valid_symbol
from users.models import User

#custom django form to purchase stocks
class PurchaseForm(forms.ModelForm):
    stock_ticker = forms.CharField(required=True, max_length=20)
    num_of_shares = forms.IntegerField(required=True)
   
    #link the form to my custom model
    class Meta:
        model = Transactions
        fields = (
            'stock_ticker',
            'num_of_shares',
        )
    def clean(self):
        cleaned_data = super(PurchaseForm, self).clean()
        stock_ticker = cleaned_data.get('stock_ticker').upper()
        num_of_shares = cleaned_data.get('num_of_shares')
        #perform validation checks on the input
        if not stock_ticker or not num_of_shares:
            raise forms.ValidationError('You have to write something.')
        isvalid = is_valid_symbol(stock_ticker)
        if not isvalid:
            raise forms.ValidationError('That is not a valid stock ticker.')
        elif num_of_shares < 1:
            raise forms.ValidationError('Please enter at least 1 share.')
        elif not type(num_of_shares) is int:
            raise forms.ValidationError('Please enter a whole number for shares.')
                
