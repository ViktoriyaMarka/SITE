from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Error_Type)
admin.site.register(Error)
admin.site.register(Question)
admin.site.register(Idea)