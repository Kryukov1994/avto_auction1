from django.contrib import admin
from .models import Auction, Buyer, Comment


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('avto', 'start_price', 'end_time', 'active')
    list_filter = ('avto', 'active', 'end_time')
    search_fields = ('avto__brand', 'avto__model')
    date_hierarchy = 'end_time'
    ordering = ('end_time',)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['auction', 'user', 'last_bid_price', 'updated_at']
    list_filter = ['auction', 'user', 'updated_at']
    search_fields = ['auction__avto__brand']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('auction', 'author', 'text', 'created_at')
    list_filter = ('auction', 'created_at')
    search_fields = ('auction__avto__brand', 'author__username')
    ordering = ('-created_at',)