from django.urls import path
from api import views


urlpatterns = [
    path('', views.QuestionList.as_view()),
    path('<int:pk>', views.QuestionDetail.as_view())
]