# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lags(models.Model):
    id_lag = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'Lags'


class Articles(models.Model):
    id_art = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    unix = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'articles'


class ArticlesHasLags(models.Model):
    id_lag = models.ForeignKey(Lags, models.DO_NOTHING, db_column='id_lag')
    id_art = models.ForeignKey(Articles, models.DO_NOTHING, db_column='id_art')

    class Meta:
        managed = False
        db_table = 'articles_has_lags'