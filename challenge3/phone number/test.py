import phonenumbers
from app import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")  #CH mean country location
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))