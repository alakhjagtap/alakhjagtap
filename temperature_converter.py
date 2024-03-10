def fahrenheit_converter():
    number = input("Please enter the degrees you would like to convert. ")
    celcius: float = (int(number)-32) *5/9
    return celcius

def celcius_converter():
    number = input("Please enter the degrees you would like to convert. ")
    fahrenheit: float = (int(number) * 9/5) + 32
    return fahrenheit
what_type = input("Would you like to convert FAHRENHEIT or CELSIUS today? ")

if what_type == "Fahrenheit" or "FAHRENHEIT":
    print(fahrenheit_converter())
elif what_type == "Celsius" or "CELSIUS":
    print(celcius_converter())