from django import forms
from stocks.models import Profile, Portfolio, Transactions

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
        stock_ticker = cleaned_data.get('stock_ticker')
        num_of_shares = cleaned_data.get('num_of_shares')
        print(stock_ticker)
        if not stock_ticker and not num_of_shares:
            raise forms.ValidationError('You have to write something.')
        
