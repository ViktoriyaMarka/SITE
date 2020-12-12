from django.db import models

# Create your models here.

class Function(models.Model):
    name                  = models.CharField(max_length=50, verbose_name='Наименование функции')
    disciption            = models.TextField(max_length=1000, verbose_name='Описание функции')
    image                  = models.ImageField(verbose_name='Изображение', upload_to='images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Функция"
        verbose_name_plural     = "Функции"

    def __str__(self):
        return self.name

class Manual(models.Model):
    name                  = models.CharField(max_length=50, verbose_name='Наименование инструкции')
    disciption            = models.TextField(max_length=1000, verbose_name='Описание инструкции')
    image                 = models.ImageField(verbose_name='Изображение', upload_to='manual/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Инструкция"
        verbose_name_plural     = "Инструкции"

    def __str__(self):
        return self.name

class System(models.Model):
    name                  = models.CharField(max_length=50, verbose_name='Наименование требований')
    disciption            = models.TextField(max_length=1000, verbose_name='Описание инструкции')
    image                 = models.ImageField(verbose_name='Изображение', upload_to='manual/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Инструкция"
        verbose_name_plural     = "Инструкции"

    def __str__(self):
        return self.name

