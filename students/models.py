from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField("date published")
    grade = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.id