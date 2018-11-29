from django.urls import path
from . import views

app_name = "reserve"

urlpatterns = [
    path('', views.reserve_mainpage, name='reserve_mainpage'),
    path('verificationlink/', views.verification_link, name='verification_link'),
]