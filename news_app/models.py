from django.db import models

class Image(models.Model):
    url=models.CharField(max_length=255)



class Event(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.ForeignKey(Image.url)
    def __str__(self):
        return self.name

