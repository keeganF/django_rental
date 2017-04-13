from django.db import models

# Create your models here.
class Boat(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    img_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def img_url(self):
        return 'boat/pictures/'+ self.img_name



