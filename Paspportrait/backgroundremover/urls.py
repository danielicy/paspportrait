
from django.urls import re_path
from backgroundremover import views
 

urlpatterns = [
    re_path(r'^$', views.test, name='test'),
    
]

 