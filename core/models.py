from django.db import models


class Widget(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=3000)
    is_active = models.BooleanField(default=True)
    icon = models.ForeignKey('Icon', on_delete=models.CASCADE, db_index=True, related_name='widget_icon')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'

    def __str__(self):
        return f'{self.title}'

class Icon(models.Model):
    title = models.CharField(max_length=50)
    uri = models.CharField(max_length=50000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'

    def __str__(self):
        return f'{self.title}'