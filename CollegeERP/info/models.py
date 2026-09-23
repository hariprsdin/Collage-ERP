from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
