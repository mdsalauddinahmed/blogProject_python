from django.db import models

# Create your models here.

class Category(models.Model):
    Category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Category
