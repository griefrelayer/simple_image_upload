from django.db import models


class MyImage(models.Model):
    file = models.ImageField(verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True)

