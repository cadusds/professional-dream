from django.contrib import admin
from blog import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = models.Profile

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    model = models.Tag

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    model = models.Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True