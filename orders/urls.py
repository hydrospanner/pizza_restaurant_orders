from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.place_order, name="order"),
    path("add_pizza", views.add_pizza, name="add pizza"),
    path('thanks', views.thanks, name='thanks'),
]
