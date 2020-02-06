

from django.contrib import admin
from django.urls import path
from dtapp1 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.wish, name='message'),
]
