from django.db import models


class Widget(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=3000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'

    def __str__(self):
        return f'{self.title}'