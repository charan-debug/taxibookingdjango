from django.contrib import admin
#from django.contrib.auth.models import User, Group #added
from .models import TripDetails
from .models import Driver
from .models import Cab



# Register your models here.

@admin.register(TripDetails)
class TripDetailsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in TripDetails._meta.get_fields()]

@admin.register(Driver)
class Driver(admin.ModelAdmin):
	list_display = ["driver_id","driver_name","driver_contact_details","cab"]
	#autocomplete_fields = ["cab"]
	#search_fields = []

						

@admin.register(Cab)
class Cab(admin.ModelAdmin):
 	list_display = ["cab_id", "cab_type"]
 

#admin.site.register(Cab)


# Unregister your models here.

#admin.site.unregister(User) #added
#admin.site.unregister(Group) #added
