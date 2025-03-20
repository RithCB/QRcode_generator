from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.hello, name="index")
]