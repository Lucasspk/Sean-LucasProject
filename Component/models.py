from django.db import models

# Create your models here.
class Component(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length='300', default='null', null=True, blank=True)
    name = models.CharField(max_length=100)
    yearReleased = models.IntegerField(default=2000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    fps1080 = models.DecimalField(max_digits=9, decimal_places=2)
    fps1440 = models.DecimalField(max_digits=9, decimal_places=2)
    fps4k = models.DecimalField(max_digits=9, decimal_places=2)
    AvgPower = models.IntegerField()
    itemDescription = models.CharField(max_length=4000000)
    def average_fps(self):
        return (self.fps1080 + self.fps1440 + self.fps4k) / 3
class GPU(Component):
    gpuClock = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    fpsrt1080 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    fpsrt1440 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    fpsrt4k = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def average_rt_fps(self):
        return (self.fpsrt1080 + self.fpsrt1440 + self.fpsrt4k)
class CPU(Component):
    score1080 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    score1440 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    appscore = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    cores = models.IntegerField()
    socket = models.CharField(max_length=80)
class PSU(Component):
    watts = models.IntegerField()
    modular = models.CharField(max_length=200)
    rating = models.CharField(max_length=280)
    psRank = models.CharField(max_length=200)
class Motherboard(Component):
    formFactor = models.CharField(max_length=20)