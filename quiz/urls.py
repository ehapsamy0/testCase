from django.urls import path
from .views import QuizApiListView,UserAnswersListCreate,UserAnswersDetailsApiView


urlpatterns = [
    path('',QuizApiListView.as_view()),
    path('answer/',UserAnswersListCreate.as_view()),
    path('answer/<int:pk>/',UserAnswersDetailsApiView.as_view()),
]