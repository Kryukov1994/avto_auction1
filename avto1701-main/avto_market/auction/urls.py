from django.urls import path, include
from django.contrib.auth import views 
from .import views 

app_name = 'auction'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('avto/<int:avto_id>/auction_create/', views.auction_create, name="auction_create"  ),
    path('auctions/', views.view_all_auctions, name='view_all_auctions'),
    path('view_user_auctions/', views.view_user_auctions, name='view_user_auctions'),
    path("edit_auction/<int:auction_id>", views.edit_auction, name="edit_auction"),
    path('create_buyer/<int:auction_id>/<int:user_id>/', views.create_buyer, name='create_buyer'),
    path('comment_create/<int:auction_id>/<int:user_id>/', views.comment_create, name='comment_create'),
    path("auction_detail/<int:auction_id>", views.auction_detail, name="auction_detail"),
    path('winner/<int:auction_id>/', views.winner, name='winner'),
    path('profile_win/<str:username>', views.profile_win, name='profile_win'),
]