from django.urls import path

from . import views

app_name = "userdoc"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:employee_id>/", views.userWelcome, name="userWelcome"),
    #path("usercreate/", views.userCreate, name="userCreate"),
    path("new/", views.new, name="new"),
]