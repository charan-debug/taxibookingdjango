from django.urls import path,include 
from taxi.user import views
from taxi.trip import urls as u


  
urlpatterns = [
         
         path('', views.index, name ='index'),
         path('', include(u)),        
         #path('test',include(u)),
        

]