from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    todo = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title


