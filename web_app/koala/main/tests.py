from django.test import TestCase
from django.urls import reverse, resolve
from .views import home_page, about_page
# Create your tests here.


class ViewTestCase(TestCase):
    
    def test_home_view(self):
        res = resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Welcome Home!")
        self.assertEqual(res.func, home_page)
        self.assertTemplateUsed(response, 'home.html')
        
        
    def test_about_view(self):
        res = resolve(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b"This is my about page and I am interested in it!!")
        self.assertEqual(res.func, about_page)