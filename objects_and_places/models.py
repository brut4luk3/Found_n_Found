from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.room_name

class Place(models.Model):
    room_of_storage = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name

class Object(models.Model):
    place_of_storage = models.ForeignKey(Place, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.object_name
