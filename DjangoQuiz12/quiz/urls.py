from django.urls import path

from quiz import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play-quiz', views.playquiz, name='play-quiz'),
    path('play-quiz-next', views.playquiznext, name='play-quiz-next'),
    path('questions', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('new', views.QuestionCreate.as_view(), name='qcreate'),
    path('edit/<int:pk>', views.QuestionUpdate.as_view(), name='qupdate'),
    path('delete/<int:pk>', views.QuestionDelete.as_view(), name='qdelete'),

    ]
