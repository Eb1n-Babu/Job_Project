from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(default="example@email.com")  # Provide a valid default or leave blank

    def __str__(self):
        return self.name