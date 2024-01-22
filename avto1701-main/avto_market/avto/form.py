from django import forms
from .models import Avto

class AvtoForm(forms.ModelForm):
    class Meta:
        model = Avto
        fields = fields = ['brand','city','model','year','price','steering','mileage','transmission','drive','fuel','description','image','active']
        

