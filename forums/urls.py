from django.urls import path
from . import views

app_name = 'forums'
urlpatterns = [
    path('', views.show_forums, name='show_forums'),
    path('<int:question_id>/', views.show_detail, name='show_detail'),
    path('create_question/', views.create_question_page, name='create_question_page'),
    path('create_question/save/', views.create_question, name='create_question'),
    path('<int:question_id>/comment/', views.create_answer, name='create_answer'),
    path('<int:question_id>/del/', views.del_question, name='del_question'),
    path('<int:question_id>/comment/<int:answer_id>/del/', views.del_answer, name='del_answer'),
]