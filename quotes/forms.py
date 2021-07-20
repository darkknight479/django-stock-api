from django import forms
from .models import Stock_Portfolio

class Stock_PortfolioForm(forms.ModelForm):
    class Meta:
        model = Stock_Portfolio
        fields = ["ticker"]

