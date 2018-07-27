from django.contrib import admin

# Register your models here.
from quiz.models import Question

admin.site.register(Question)
