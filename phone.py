import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

Phonenumber=input("Enter Phone Number:")
number=phonenumbers.parse(Phonenumber)
print(phonenumbers.is_valid_number(number))
print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))
print(timezone.time_zones_for_number(number))
