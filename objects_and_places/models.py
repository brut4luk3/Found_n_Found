from django.db import models

class Place(models.Model):
    place_name = models.CharField(max_length=200)
    room = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name

class Object(models.Model):
    place_of_storage = models.ForeignKey(Place, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.object_name
