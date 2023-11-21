from django.db import models


class Note(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    content = models.TextField(blank=True, verbose_name='Note content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
