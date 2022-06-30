from django.db import models
from django.contrib.auth.models import User
from taxi.trip.choices import CabTypes,TripStatus

# Create your models here.

class TripDetails(models.Model):
	trip_id = models.IntegerField(primary_key=True)  
	customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	#source=models.CharField(max_length=200)
	source=models.TextField(null=True,blank=True)
	destination=models.TextField(null=True,blank=True)
	date=models.DateTimeField(auto_now_add=True)
	driver=models.ForeignKey('Driver',on_delete=models.CASCADE,null=True,blank=True)
	# cab=models.ForeignKey('Cab',on_delete=models.CASCADE,null=True,blank=True)
	trip_status=models.PositiveSmallIntegerField(choices=TripStatus.choices,default = TripStatus.AVAILABLE)


	def __str__(self):
		return self.source

class Driver(models.Model):
	driver_id = models.IntegerField(primary_key=True)  
	driver_name=models.CharField(max_length=50)
	#driver_address=models.TextField(null=True,blank=True)
	driver_contact_details=models.IntegerField(null=True)
	cab=models.ForeignKey('Cab',on_delete=models.CASCADE,null=True,blank=True)

	#trip_info=models.ForeignKey('TripDetails',on_delete=models.CASCADE)

	def __str__(self):
		return self.driver_name

class Cab(models.Model):
	# CAB_TYPES = (
 #        ('MINI', 'Mini'),
 #        ('PRIME', 'Prime'),
 #        ('SUV', 'Suv'),
 #        ('BIKE', 'Bike'),
 #        ('AUTO', 'Auto'),
    # )
	cab_id = models.IntegerField(primary_key=True)  
	cab_type=models.PositiveSmallIntegerField(choices = CabTypes.choices,null=True,blank =True)
	#cab_address=models.TextField(null=True,blank=True)
	
	


	# def __str__(self):
	# 	return self.cab_type

