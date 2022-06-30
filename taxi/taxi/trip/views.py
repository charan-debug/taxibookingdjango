from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from taxi.trip.models import Driver,TripDetails
from taxi.trip.choices import CabTypes,TripStatus
from taxi.user.views import Login 
from django.contrib.auth.models import  User
from django.shortcuts import render



# Create your views here.
def tripdetails(request):
	return HttpResponse("Welcome to CHERRY TAXI")



def validate(request):
   if request.method == 'POST':
      source= request.POST["source"]
      destination = request.POST["destination"]
      cab = request.POST["cab"]

     
      current_user=request.user
      user_id=current_user.id
      user_name=current_user.username

      


      dict = {
         'source': source,
         'destination': destination,
         'cab': cab
      }

      dict1 = {
      "MINI":1 ,
      "PRIME" :2,
      "SUV" :3,
      "BIKE" :4,
      "AUTO" : 5,
      }
      
      cab_temp = dict.get('cab')
      cab_int = dict1.get(cab_temp)
      driver = Driver.objects.get(cab__cab_type=cab_int)

    


      trip = TripDetails.objects.create(source=dict.get('source'),destination=dict.get('destination'),driver =driver,customer=request.user)

      
      driver_name = driver.driver_name
      driver_number = driver.driver_contact_details
    

      dict["driver"]=driver_name
      dict["driver_num"]=driver_number

      d=TripDetails.objects.filter(trip_status=TripStatus.STARTED,driver__driver_name=driver_name).order_by("-date")
      if d.exists():
         print("driver is not available")
         print(d)
         return render(request,'trip/tryagain.html')  
          

      
      return render(request, 'trip/validate.html', dict)  




def success(request):

   trip=TripDetails.objects.filter(customer=request.user).order_by("-date")
   if trip.exists():
      trip = trip.first()
      trip.trip_status=TripStatus.STARTED
      trip.save()
   
   return render(request, 'trip/success.html')  


def complete(request):
  
   trip=TripDetails.objects.filter(customer=request.user).order_by("-date")
   if trip.exists():
      trip = trip.first()
      trip.trip_status=TripStatus.DONE
      trip.save()
   return render(request, 'trip/index.html')     



def history(request):
        
         hist=TripDetails.objects.filter(customer=request.user)
         hist_dict = {
            
            'hist':hist
         }
         

         return render(request,'trip/history.html', hist_dict)     

     
