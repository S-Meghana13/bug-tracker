from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bug(models.Model):

    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    STATUS_CHOICES = [
        ('Open','Open'),
        ('In Progress','In Progress'),
        ('Resolved','Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title