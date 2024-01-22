from django.db import models
from django.contrib.auth.models import User
from avto.models import Avto
from django.core.exceptions import ValidationError
from django.shortcuts import redirect



class Auction(models.Model):
    avto = models.OneToOneField(Avto, on_delete=models.CASCADE, related_name='auction')
    start_price = models.DecimalField(max_digits=15, decimal_places=2)
    end_time = models.DateTimeField(help_text='YYYY-MM-DD HH:MM:SS')
    active = models.BooleanField(default=True)

    def __str__(self):
        return  self.avto.brand


class Buyer(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='buyers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_bid_price = models.DecimalField(max_digits=15, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
   
        
    def __str__(self):
        return str(self.last_bid_price)
    
    class Meta:
        ordering = ['-last_bid_price']
    
class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']