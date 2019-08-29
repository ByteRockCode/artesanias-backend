from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Store(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='owner_classrooms',
        verbose_name='dueño',
    )

    name = models.CharField('nombre', max_length=255)
    slug = models.SlugField('slug', blank=True, unique=True)
    description = models.TextField('descripción')

    def __str__(self):
        return self.name
