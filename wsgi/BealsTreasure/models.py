from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Values(models.Model):
    exp_x = models.BigIntegerField()
    exp_y = models.BigIntegerField()
    base = models.BigIntegerField(blank=True, null=True)
    max_base = models.BigIntegerField()

    class Meta:
        db_table = 'exp_values'


class Attempts(models.Model):
    valuekey = models.ForeignKey('Values', db_column='ValueKey')
    start_time = models.DateTimeField(db_column="Timestamp", auto_now_add=True)

    class Meta:
        db_table = 'attempts'


class Verifys(models.Model):
    attemptkey = models.ForeignKey('Attempts', db_column='AttemptKey')
    
    finish_time = models.DateTimeField(db_column="Timestamp", 
                                       auto_now_add=True)
    
    user_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'verifys'
