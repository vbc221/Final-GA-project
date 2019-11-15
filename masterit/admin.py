from django.contrib import admin
from .models import Category, Subject, Subject2,Help
# Register your models here.

admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Subject2)
admin.site.register(Help)