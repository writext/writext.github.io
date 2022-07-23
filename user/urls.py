from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('registr/', views.reg_page, name='reg_page'),
    path('registr/reg/', views.reg, name='reg'),
]