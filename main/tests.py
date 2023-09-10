from django.test import TestCase, Client
from main.models import Main

class mainTestCase (TestCase):
    def setUp(self):
        Main.objects.create(name="Tempat minum", amount= 0,
                            description="tempat minum murah",
                            rating="7/10",
                            reviews= "Sebanding dengan harga")
    def test_main_model(self):
        main_obj = Main.objects.get(name="Tempat minum")
        self.assertEqual(main_obj.amount, 0)
        self.assertEqual(main_obj.description, "tempat minum murah")
        self.assertEqual(main_obj.rating, "7/10")
        self.assertEqual(main_obj.reviews, "Sebanding dengan harga")

# Create your tests here.
