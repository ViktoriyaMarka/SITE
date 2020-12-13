from django.db import models
from django.utils.translation import gettext as _


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

class System_App(models.Model):
    name                  = models.CharField(max_length=100, verbose_name='Наименование требований')
    CPU                   = models.CharField(max_length=50, verbose_name='CPU')
    RAM                   = models.CharField(max_length=50, verbose_name='RAM')
    HDD_SSD               = models.CharField(max_length=50, verbose_name='HDD_SSD')
    Video                 = models.CharField(max_length=50, verbose_name='Видеоадаптер', null=True, blank=True)
    NetworkCard           = models.CharField(max_length=50, verbose_name='Сетевая карта')
    Manipulators          = models.CharField(max_length=200, verbose_name='Манипуляторы', null=True, blank=True)

    
    class Meta:
        verbose_name            = "Системные аппаратные требования"
        verbose_name_plural     = "Системные аппаратные требования"

    def __str__(self):
        return self.name

class System_Prog(models.Model):
    name                  = models.CharField(max_length=100, verbose_name='Наименование требований')
    OS                    = models.CharField(max_length=50, verbose_name='OS')
    DOP                   = models.CharField(max_length=50, verbose_name='Дополнительное ПО или СУБД')

    
    class Meta:
        verbose_name            = "Системные программные требования"
        verbose_name_plural     = "Системные программные требования"

    def __str__(self):
        return self.name

class File(models.Model):
    name                  = models.CharField(max_length=50, verbose_name='Версия программы')
    file_prog             = models.FileField(_("Установщик программы"), upload_to=None, max_length=100)
    date                  = models.DateTimeField(max_length=50, verbose_name='Дата добавления', null=True, auto_now_add=True)
    
    class Meta:
        get_latest_by           = "date"
        verbose_name            = "Программа"
        verbose_name_plural     = "Версии программы"

    def __str__(self):
        return self.name

