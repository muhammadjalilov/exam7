from django.db import models

class Vacancy(models.Model):
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.salary}'
