from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_item_description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.first_name