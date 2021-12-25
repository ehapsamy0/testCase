from django.contrib import admin
from .models import Question,Quiz,Answer,TypeQuestion,UserAnswers
# Register your models here.



admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(TypeQuestion)
admin.site.register(UserAnswers)