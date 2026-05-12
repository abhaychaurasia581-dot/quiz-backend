
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Question, Option
from .serializers import QuestionSerializer, OptionSerializer,StudentSerializer
from rest_framework.decorators import api_view
from .models import Student




@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all().order_by('-created_at')
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = Question.objects.create(text=request.data['text'])
            for opt in request.data.get('options', []):
                Option.objects.create(
                    question=question,
                    text=opt['text'],
                    is_correct=opt.get('is_correct', False)
                )
            return Response(QuestionSerializer(question).data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)