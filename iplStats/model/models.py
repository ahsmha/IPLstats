from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'teams'
