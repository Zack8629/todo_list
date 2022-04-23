from django.db import models


class Task(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    task_text = models.TextField()
    is_done = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-username']

    def __str__(self):
        return f'Задача {self.id}'
