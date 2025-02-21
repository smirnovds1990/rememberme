from django.contrib import admin

from .models import Article, Tag, Topic


admin.site.register([Article, Tag, Topic])
