
from django.db import models


class Circuit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=9000)
    location = models.CharField(max_length=9000)
    country = models.CharField(max_length=9000)
    alt = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuit'


class Constructor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=9000)
    nationality = models.CharField(max_length=9000)

    class Meta:
        managed = False
        db_table = 'constructor'


class Driver(models.Model):
    name = models.CharField(max_length=9000)
    surname = models.CharField(max_length=9000)
    code = models.CharField(max_length=3, blank=True, null=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=9000)
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
    name = models.CharField(max_length=9000)
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
    status = models.CharField(max_length=9000, blank=True, null=True)
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
