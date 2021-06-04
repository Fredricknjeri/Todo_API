from django.contrib import admin

# Register your models here.
from snippets.models import Todo

admin.site.register(Todo)