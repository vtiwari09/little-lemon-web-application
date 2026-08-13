from django.test import TestCase
from .models import Menu, Booking


class MenuModelTest(TestCase):

    def test_menu_creation(self):
        menu = Menu.objects.create(
            name="Pasta",
            price=12.50,
            menu_item_description="Fresh homemade pasta"
        )

        self.assertEqual(menu.name, "Pasta")
        self.assertEqual(menu.price, 12.50)
        self.assertEqual(
            menu.menu_item_description,
            "Fresh homemade pasta"
        )


class BookingModelTest(TestCase):

    def test_booking_creation(self):
        booking = Booking.objects.create(
            first_name="Vishal",
            reservation_date="2026-08-20",
            reservation_slot=19,
            number_of_guests=2
        )

        self.assertEqual(booking.first_name, "Vishal")
        self.assertEqual(booking.reservation_slot, 19)
        self.assertEqual(booking.number_of_guests, 2)