from django.test import TestCase
from .models import Menu, Booking

class MenuModelTest(TestCase):

    def test_create_menu(self):
        item = Menu.objects.create(
            title="Pizza",
            price=250,
            inventory=10
        )

        self.assertEqual(item.title, "Pizza")
        self.assertEqual(item.price, 250)


class BookingModelTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Piyush",
            no_of_guests=4,
            booking_date="2026-07-04"
        )

        self.assertEqual(booking.name, "Piyush")