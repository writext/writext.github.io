from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.show_post, name='show_post'),
    #path('video/', views.show_post, name='show_post'),
    path('<int:post_id>/', views.show_detail, name='show_detail'),
    path('create_post/', views.create_post_page, name='create_post_page'),
    path('create_post/save/', views.create_post, name='create_post'),
    path('<int:post_id>/comment/', views.create_comment, name='create_comment'),
    path('<int:post_id>/del/', views.del_post, name='del_post'),
    path('<int:post_id>/comment/<int:comment_id>/del/', views.del_comment, name='del_comment'),
]