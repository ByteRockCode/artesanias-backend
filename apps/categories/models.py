from django.db import models


class Category(models.Model):
    name = models.CharField('nombre', max_length=255)
    slug = models.SlugField('slug', blank=True, unique=True)
    description = models.TextField('descripción')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
