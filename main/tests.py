from django.test import TestCase
from django.urls import reverse
from main.models import Product

class mainTestCase (TestCase):
    def setUp(self): # test case mengisi data dan melihat jika sudah tersimpan dengan benar
        Product.objects.create(item_name="Tempat minum", amount= 0,
                            description="tempat minum murah",
                            rating="7",
                            reviews= "Sebanding dengan harga")
    def test_main_model(self):
        main_obj = Product.objects.get(item_name="Tempat minum")
        self.assertEqual(main_obj.amount, 0)
        self.assertEqual(main_obj.description, "tempat minum murah")
        self.assertEqual(main_obj.rating, "7")
        self.assertEqual(main_obj.reviews, "Sebanding dengan harga")

    def test_show_main_view(self): # test case mengecek jika show_main sudah benar
        response = self.client.get(reverse('main:show_main')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Neva Denstia Shabira')
        self.assertContains(response, '2206083073')
        self.assertContains(response, 'PBP B')




# Create your tests here.
