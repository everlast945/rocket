from django.db import models

# Create your models here.
# Требуется создать python веб-сервис. В качестве основы необходимо использовать один из веб-
# фреймворков: flask(предпочтительно), django, tornado
#
# Сервис должен предоставлять возможность редактирования регионов и городов, которые входят в
# регионы.


from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Region(MPTTModel):
    """
    Модель Региона
    """
    name = models.CharField('Наименование', max_length=30)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Town(models.Model):
    """
    Модель Города
    """
    name = models.CharField('Наименование', max_length=30)
    region = models.ForeignKey(Region, verbose_name='Регион', related_name='towns', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


