#pip install opencage
#pip install folium
import phonenumbers
import opencage
import folium
from my_number import number
from phonenumbers import geocoder

ph_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ph_number, "en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = "d24ba1adc02747c198d7ad9397a29492"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat, lng)

my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

my_map.save("mylocation.html")