from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _

class CabTypes(IntegerChoices):
        MINI = 1, _('Mini')
        PRIME = 2, _('Prime')
        SUV = 3, _('Suv')
        BIKE = 4, _('Bike')
        AUTO = 5, _('Auto')


class TripStatus(IntegerChoices):
	STARTED = 0, _('Started')
	DONE = 1, _('Done')
	ERROR = 2, _('Error')
	AVAILABLE = 3, _('Available')