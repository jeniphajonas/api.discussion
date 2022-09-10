from django.contrib import admin

# Register your models here.

from .models import (Mapindi,MapindiSeason,MapindiUserVote,MapindiVideoComment)


@admin.register(Mapindi)
class Category(admin.ModelAdmin):
    list_display = ["user_id", "season_id","winner_status","vote","first_name","last_name","school_name","school_location",
        "subject_name" ,"class_name" ,"lesson" ,"description","video_id","date_uploaded","status"]
    search_fields = ["user_id", "season_id","winner_status","vote","first_name","last_name","school_name","school_location",
        "subject_name" ,"class_name" ,"lesson" ,"description","video_id","date_uploaded","status"]
    list_filter = ["user_id", "season_id","winner_status","vote","first_name","last_name","school_name","school_location",
        "subject_name" ,"class_name" ,"lesson" ,"description","video_id","date_uploaded","status"]

@admin.register(MapindiSeason)
class Category(admin.ModelAdmin):
    list_display = ["season_name","open_close_status","start_date", "end_date", "date_added"]
    search_fields = ["season_name","open_close_status","start_date", "end_date", "date_added"]
    list_filter = ["season_name","open_close_status","start_date", "end_date", "date_added"]

@admin.register(MapindiUserVote)
class Category(admin.ModelAdmin):
    list_display = ["user_id","video_id","date_added"]
    search_fields = ["user_id","video_id","date_added"]
    list_filter = ["user_id","video_id","date_added"]

@admin.register(MapindiVideoComment)
class Category(admin.ModelAdmin):
    list_display = ["user_id","video_id","content","date_added"]
    search_fields = ["user_id","video_id","content","date_added"]
    list_filter = ["user_id","video_id","content","date_added"]            