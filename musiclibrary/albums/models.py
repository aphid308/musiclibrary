from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=120)
    website = models.URLField(null=True)
    mbid = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=120)
    website = models.URLField(null=True)
    mbid = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist)
    label = models.ForeignKey(Label)
    mbid = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s, by %s" % (self.title, self.artist)


