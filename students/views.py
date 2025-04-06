from rest_framework import viewsets, generics

from students.models import Student
from students.serializer import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentsSerializer

class StudentsByIdViewSet(generics.RetrieveUpdateAPIView):
    queryset =  Student.objects.all()
    serializer_class = StudentsSerializer
    partial = True
