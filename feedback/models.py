from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Error_Type(models.Model):
    error_type                  = models.CharField(max_length=50, verbose_name='Тип ошибки')
    
    class Meta:
        verbose_name            = "Тип ошибки"
        verbose_name_plural     = "Типы ошибки"

    def __str__(self):
        return self.error_type

class Error(models.Model):
    email                 = models.EmailField(_("Почта"), max_length=254)
    name                  = models.ForeignKey(Error_Type, verbose_name=_("Тип ошибки"), on_delete=models.DO_NOTHING)
    disciption            = models.TextField(max_length=1000, verbose_name='Описание ошибки')
    image                 = models.ImageField(verbose_name='Изображение', upload_to='images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Ошибка"
        verbose_name_plural     = "Ошибки"

    def __str__(self):
        return self.name.error_type

class Question(models.Model):
    email                 = models.EmailField(_("Почта"), max_length=254)
    name                  = models.CharField(max_length=50, verbose_name='Тема вопроса')
    disciption            = models.TextField(max_length=1000, verbose_name='Описание вопроса')
    image                 = models.ImageField(verbose_name='Изображение', upload_to='images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Вопрос"
        verbose_name_plural     = "Вопросы"

    def __str__(self):
        return self.name

class Idea(models.Model):
    email                 = models.EmailField(_("Почта"), max_length=254)
    name                  = models.CharField(max_length=50, verbose_name='Идея')
    disciption            = models.TextField(max_length=1000, verbose_name='Описание идеи')
    image                 = models.ImageField(verbose_name='Изображение', upload_to='images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        verbose_name            = "Идея"
        verbose_name_plural     = "Идеи"

    def __str__(self):
        return self.name