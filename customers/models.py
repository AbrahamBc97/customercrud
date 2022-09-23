from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    address = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - by ' + self.user.username
