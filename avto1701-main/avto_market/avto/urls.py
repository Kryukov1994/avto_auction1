from django.urls import path
from .import views

app_name = 'avto'

urlpatterns = [
    path("", views.index, name="index"),
    path("avto_list/", views.avto_list, name="avto_list"),
    path("avto_detail/<int:avto_id>", views.avto_detail, name="avto_detail"),
    path("new_avto/", views.new_avto, name="new_avto"),
    path("user_avto/", views.user_avto, name="user_avto"),
    path("edit_avto/<int:avto_id>", views.edit_avto, name="edit_avto"),
    path("delete_avto/<int:avto_id>", views.delete_avto, name="delete_avto"),
]
