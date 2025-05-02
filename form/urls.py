from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ajax/check-user/', views.check_user_exists, name='check_user_exists'),

]
