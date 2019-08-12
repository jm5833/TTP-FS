from django import forms

#custom django form to purchase stocks
class PurchaseForm(forms.Form):
    symbol = forms.CharField(required=True, max_length=20)
    quantity = forms.IntegerField(required=True)
    
    def clean(self):
        cleaned_data = super(PurchaseForm, self).clean()
        symbol = cleaned_data.get('symbol')
        quantity = cleaned_data.get('quantity')
        if not symbol and not quantity:
            raise forms.ValidationError('You have to write something.')
        
