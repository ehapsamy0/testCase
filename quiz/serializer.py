from rest_framework import serializers
from .models import Question,Quiz,Answer,TypeQuestion,UserAnswers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'





class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'


    def get_answers(self,obj):
        try:
            answers = obj.answer_set.all()
            serializer = AnswerSerializer(answers,many=True)
            return serializer.data
        except:
            return False





class TypeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeQuestion
        fields = '__all__'


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = '__all__'





class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'



    def get_questions(self,obj):
        answers = obj.question_set.all()
        serializer = QuestionSerializer(answers,many=True)
        return serializer.data






