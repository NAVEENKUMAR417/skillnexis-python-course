def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


choice = input("Enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius: ")

if choice == "1":
    temperature = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", result)

elif choice == "2":
    temperature = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")