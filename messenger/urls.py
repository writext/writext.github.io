from django.urls import path
from . import views

app_name = 'messenger'
urlpatterns = [
    path('users/', views.show_users, name='show_users'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/chat/', views.chat, name='chat'),
    path('users/<int:user_id>/chat/<str:message_text>/send/', views.message_send, name='message_send'),
    path('users/<int:user_id>/chat/<int:message_id>/del/', views.message_del, name='message_del'),
]