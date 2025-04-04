from django.contrib.auth.models import Group, User
from rest_framework import serializers

from students.models import Student


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'grade', 'phone', 'email']