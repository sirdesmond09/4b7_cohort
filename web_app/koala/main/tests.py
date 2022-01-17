from django.test import TestCase
from django.urls import reverse, resolve
from .views import home_page, contact_us
# Create your tests here.


class ViewTestCase(TestCase):
    
    def test_home_view(self):
        res = resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        # print(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Welcome to MulZact Store")
        self.assertEqual(res.func, home_page)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'ecommerce.css')
        
    def test_contact_view(self):
        res = resolve(reverse("contact"))
        response = self.client.get(reverse("contact"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "LinkedIn")
        self.assertEqual(res.func, contact_us)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'ecommerce.css')