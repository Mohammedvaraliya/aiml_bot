from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.text