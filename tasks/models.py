from django.db import models


class Task(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    task_text = models.TextField()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
