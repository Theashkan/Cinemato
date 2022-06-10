from django.contrib import admin
from posts.models import *

@admin.register(card)
class cardAdmin(admin.ModelAdmin):
    list_display = ("title" , "slug", "status", "author", "published_at")
    preppopulated_fields = {"slug": ("title,")}
    search_fields = ["title", "body"]
    oredering = {'-published_at'}
    list_filter = ["status"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass