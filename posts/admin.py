from django.contrib import admin
from .models import Post


# This will make the Post accessable from the Admin site
admin.site.register(Post)


# Register your models here.
