from django.db import models
from django.core.urlresolvers import reverse

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Artist(TimeStampedModel):
    name = models.CharField(max_length=120)
    website = models.URLField(null=True)
    mbid = models.CharField(max_length=40)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name

class Label(TimeStampedModel):
    name = models.CharField(max_length=120)
    website = models.URLField(null=True)
    mbid = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Album(TimeStampedModel):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist, db_index=True)
    label = models.ForeignKey(Label, db_index=True)
    mbid = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s, by %s" % (self.title, self.artist)



        
