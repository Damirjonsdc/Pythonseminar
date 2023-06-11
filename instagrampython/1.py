import phonenumbers1
from phonenumbers2 import geocoder
phone_number1 = phonenumbers.parse("+998911004525")
phone_number2 = phonenumbers1.parse("+998972773300")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"))

