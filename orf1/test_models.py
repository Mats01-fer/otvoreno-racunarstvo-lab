# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Circuit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    location = models.CharField(max_length=-1)
    country = models.CharField(max_length=-1)
    alt = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit'


class Constructor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=-1)
    nationality = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'constructor'


class Driver(models.Model):
    name = models.CharField(max_length=-1)
    surname = models.CharField(max_length=-1)
    code = models.CharField(max_length=3, blank=True, null=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=-1)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'driver'


class Driverinseason(models.Model):
    number = models.IntegerField()
    driverid = models.OneToOneField(Driver, models.DO_NOTHING, db_column='driverid', primary_key=True)
    year = models.ForeignKey('Season', models.DO_NOTHING, db_column='year')
    constructorid = models.ForeignKey(Constructor, models.DO_NOTHING, db_column='constructorid')

    class Meta:
        managed = False
        db_table = 'driverinseason'
        unique_together = (('driverid', 'year', 'constructorid'),)


class Grandprix(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    year = models.IntegerField()
    round = models.IntegerField()
    circuitid = models.ForeignKey(Circuit, models.DO_NOTHING, db_column='circuitid')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'grandprix'


class Raceresult(models.Model):
    fastestlaptime = models.FloatField(blank=True, null=True)
    grid = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    laps = models.IntegerField(blank=True, null=True)
    time = models.FloatField(blank=True, null=True)
    fastestlap = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    driverid = models.ForeignKey(Driverinseason, models.DO_NOTHING, db_column='driverid')
    year = models.IntegerField(blank=True, null=True)
    constructorid = models.IntegerField()
    gpid = models.ForeignKey(Grandprix, models.DO_NOTHING, db_column='gpid')

    class Meta:
        managed = False
        db_table = 'raceresult'


class Season(models.Model):
    year = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'season'
