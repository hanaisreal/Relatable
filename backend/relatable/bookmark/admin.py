from django.contrib import admin
from .models import Bookmark
from .models import Like
# Register your models here.
admin.site.register(Bookmark)
admin.site.register(Like)