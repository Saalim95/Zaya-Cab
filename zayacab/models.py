from django.db import models
from django.contrib.auth.models import User
  
class Driver(models.Model):
    
    STATUS_OPTIONS = (
        ('AV', 'AVAILABLE'),
        ('OFF', 'OFFLINE'),
        ('BK', 'BOOKED')
    )

    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default="AV")

    def __str__(self):
        return str(self.name)

class Commuter(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def __str__(self) :
        return str(self.name)

class Trip(models.Model):
    commuter = models.ForeignKey(Commuter, null=True, related_name='commuter', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, null=True, related_name='driver', on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    fare = models.FloatField(null=True)

    def __str__(self):
        FromTo = self.source + "-" + self.destination
        return FromTo