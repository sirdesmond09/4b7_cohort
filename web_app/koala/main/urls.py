from django.urls import path
from .views import contact_us, home_page

urlpatterns = [
    path('home/', home_page, name="home"),
    path("contact_us/", contact_us, name='contact')
]