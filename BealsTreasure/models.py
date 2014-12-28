from django.db import models

# Create your models here.

class Values(models.Model):
    exp_m = models.BigIntegerField()
    exp_n = models.BigIntegerField()
    base_x = models.BigIntegerField(blank=True, null=True)
    max_base = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'values'


class Attempts(models.Model):
    valuekey = models.ForeignKey('Values', db_column='ValueKey')
    start_time = models.DateTimeField(db_column="Timestamp", auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'attempts'


class Verifys(models.Model):
    attemptkey = models.ForeignKey('Attempts', db_column='AttemptKey')
    finish_time = models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    user_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'uc_verifys'
