from django.contrib import admin

# Register your models here.

from .models import List
from .models import Content

admin.site.register(List)
admin.site.register(Content)