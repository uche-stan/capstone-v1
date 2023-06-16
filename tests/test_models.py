from django.test import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="icecreame", price=80, inventory=100)
        self.assertEqual(item,"icecreame: 80")
        