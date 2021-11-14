from django.contrib import admin

from .models import Choice, Question

# adding the option to be able to add question through the admin portal
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
