from django.urls import path, include
from django.contrib.auth import views 
from .import views 


app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"  ),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('messages_view/', views.messages_view, name='messages_view'),
    path("messages_detail/<int:messages_id>", views.messages_detail, name="messages_detail"),
    path("send_message/", views.send_message, name="send_message"),
    path("change_password/", views.change_password, name="change_password"),
    path("password_change_done/", views.password_change_done, name="password_change_done"),
    
]