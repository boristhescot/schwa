
from django.urls import path, include
from schwa_app import views


urlpatterns = [
    path('', views.schwa_home, name='schwa_home'),
    path('save_recording', views.save_recording, name='save_recording')
]