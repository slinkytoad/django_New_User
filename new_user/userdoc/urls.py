from django.urls import path

from . import views

app_name = "userdoc"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<slug:slug>/", views.userWelcome, name="userWelcome"),
]