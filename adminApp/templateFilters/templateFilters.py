from django import template
from cryptography.fernet import Fernet
import base64
from django.conf import settings
from django.db.models import Sum, F

from adminApp.models import Hospital, BedBooking

register = template.Library()

@register.filter(name='encData')
def encData(data):
    try:
        if(data):
            toStr = str(data)
            cipher_suite = Fernet(settings.ENC_KEY)
            encrypted_text = cipher_suite.encrypt(toStr.encode('ascii'))
            encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
            return encrypted_text
        else:
            return None
    except Exception as e:
        return None

@register.simple_tag
def get_beds(hospital_id):
    total_beds = Hospital.objects.get(pk=hospital_id).available_beds
    booked_beds = BedBooking.objects.filter(hospital=hospital_id).exclude(status__in=[3,4]).aggregate(booked_beds=Sum(F('bed_booked')))[
        'booked_beds']
    if (total_beds is None):
        total_beds = 0
    if (booked_beds is None):
        booked_beds = 0
    availabe_beds = total_beds - booked_beds
    return availabe_beds