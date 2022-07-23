from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    #path('lents/', views.lents_page, name='lents_page'),
    #path('videolents/', views.videolents_page, name='videolents_page'),
    path('forum/', views.forum_page, name='forum_page'),
    path('cloud/', views.cloud_page, name='cloud_page'),
    path('autherror/', views.auth_error, name='auth_error'),
]