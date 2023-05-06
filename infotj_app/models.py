from django.db import models
from PIL import Image


class Establishment(models.Model):
    establishment_choices= (
        ('M', 'Медицина'),
        ('P', 'Парки и места отдыха'),
        ('K', 'Культура и кино'),
        ('S', 'Покупка'),
        ('A', 'Авто'),
        ('U', 'Учёба'),
        ('F', 'Питание'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    type_of_establishment = models.CharField(max_length=1, choices=establishment_choices)
    address_street = models.CharField(max_length=255)
    address_number = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    second_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    business_hours = models.CharField(max_length=255)
    photos = models.ManyToManyField('Photo', related_name='establishments', through='EstablishmentPhoto')

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='establishment_photos/')

class EstablishmentPhoto(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)