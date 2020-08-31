from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class ContactDetail(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=50)


class Institution(models.Model):
    name = models.CharField(max_length=30)
    additional_info = models.CharField(max_length=60, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Qualification(models.Model):
    name = models.CharField(max_length=40)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    subskills = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Experience(models.Model):
    role_name = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

