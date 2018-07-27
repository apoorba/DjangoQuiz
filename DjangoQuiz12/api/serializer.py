from rest_framework import serializers

from quiz import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question_text', 'category')
        model = models.Question
