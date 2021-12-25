from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Question,Quiz,Answer,TypeQuestion,UserAnswers
from .serializer import QuizSerializer,QuestionSerializer,AnswerSerializer,UserAnswersSerializer,TypeQuestionSerializer



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3

class QuizApiListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination



class UserAnswersListCreate(generics.ListCreateAPIView):
    serializer_class = UserAnswersSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        request = self.request
        user = request.user

        quiz_id = request.query_params.get('quiz_id',1)
        quiz = Quiz.objects.get(id=quiz_id)
        queryset = UserAnswers.objects.filter(user=user,submited=False,quiz=quiz)

        return queryset




class UserAnswersDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAnswersSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserAnswers.objects.filter(submited=False)



