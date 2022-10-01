from django.contrib import admin
from .models import Todo
from django.contrib.auth.models import User

# Register your models here.
admin.site.unregister(User)
admin.site.register(Todo)
admin.site.register(User)