from django import forms
from .models import Auction, Buyer, Comment

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['start_price','active', 'end_time', ]
        

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['last_bid_price']

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)