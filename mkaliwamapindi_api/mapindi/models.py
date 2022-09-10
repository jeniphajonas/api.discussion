# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mapindi(models.Model):
    user_id = models.IntegerField()
    season_id = models.IntegerField()
    winner_status = models.IntegerField()
    vote = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=50)
    school_location = models.CharField(max_length=25)
    subject_name = models.CharField(max_length=25)
    class_name = models.CharField(max_length=255)
    lesson = models.CharField(max_length=100)
    description = models.TextField()
    video_id = models.CharField(max_length=15)
    date_uploaded = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = 'mapindi'


class MapindiSeason(models.Model):
    season_name = models.CharField(max_length=255)
    open_close_status = models.IntegerField()
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'mapindi_season'


class MapindiUserVote(models.Model):
    user_id = models.IntegerField()
    video_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'mapindi_user_vote'


class MapindiVideoComment(models.Model):
    user_id = models.IntegerField()
    video_id = models.IntegerField()
    content = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'mapindi_video_comment'
