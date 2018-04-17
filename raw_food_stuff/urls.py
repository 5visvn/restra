from django.conf.urls import url
from raw_food_stuff import views

urlpatterns = [
   url(r'login/', views.login),
]
