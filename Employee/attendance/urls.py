from django.urls import path
from . import views

urlpatterns = [
    path("", views.calender),
    path("/new_user", views.new_user, name='new-user')
]
