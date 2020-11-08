from django.contrib import admin

from .models import Article, Comment, Vote

admin.site.register(Vote)
admin.site.register(Article)
admin.site.register(Comment)
