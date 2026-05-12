
from rest_framework import serializers
from .models import Question, Option
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = ['id', 'name', 'age', 'roll_number', 'created_at']




class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)   

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']