from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class test_Snacks(SimpleTestCase):
    def test_home_stats(self):
        url= reverse('home')
        response=self.client.get(url)
        print(response)
        self.assertEqual(response.status_code,200)

    def test_home_template(self):
        url= reverse('home')
        response=self.client.get(url)
        print(response)
        self.assertTemplateUsed(response, 'home.html')
    def test_about_stats(self):
        url= reverse('about')
        response=self.client.get(url)
        print(response)
        self.assertEqual(response.status_code,200)
    def test_about_template(self):
        url= reverse('about')
        response=self.client.get(url)
        print(response)
        self.assertTemplateUsed(response, 'about.html')

