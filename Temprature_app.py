
def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = 5/9*(fahrenheit_temp-32)
    return celsius_temp


def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp


def kelvin_to_celsius(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    return celsius_temp

  
def celsius_to_kelvin(celsius_temp):
    kelvin_temp = celsius_temp + 273.15
    return kelvin_temp


def fahrenheit_to_kelvin(fahrenheit_temp):
  kelvin_temp = (fahrenheit_temp - 32) * (5/9) + 273.15
  return kelvin_temp


def kelvin_to_fahrenheit(kelvin_temp):
  fahrenheit_temp = (kelvin_temp - 273.15) * (9/5) + 32
  return fahrenheit_temp


# main body of the code

def main():

 print("🌡️ Welcome to the Temperature Converter! 🌡️")

 while True:
        
        # Displaying options to the user

        print("Choose a conversion:")
        
        print("1. Fahrenheit → Celsius")

        print("2. Celsius → Fahrenheit")

        print("3. Kelvin → Celsius")

        print("4. Celsius → Kelvin")

        print("5. Fahrenheit → Kelvin")

        print("6. Kelvin → Fahrenheit")
    
    
    # OUTPUT BLOCK 

        # taking users input 

        choice = int(input(" PLESE ENTER YOUR CHOICE [ 1-6 ] "))

        if choice == 1 :
           fahrenheit_temp = float ( input ("enter temp in °F "))
           Result = fahrenheit_to_celsius(fahrenheit_temp)
           print(f"{ fahrenheit_temp }°F = { Result:.2f}°C ")


        elif choice == 2 :
           celsius_temp = float ( input ( " enter temp in °c"))
           Result = celsius_to_fahrenheit(celsius_temp)
           print(f"{celsius_temp}°C = {Result:.2f}°F ")


        elif choice == 3 :
           kelvin_temp = float ( input ( " enter temp in K "))
           Result = kelvin_to_celsius(kelvin_temp)
           print(f"{kelvin_temp} K  = {Result:.2f}°C ")


        elif choice == 4 :
            celsius_temp = float ( input ( " enter temp in °C "))
            Result = celsius_to_kelvin(celsius_temp)
            print(f"{celsius_temp}°C = {Result:.2f} K ")


        elif choice == 5 :
           fahrenheit_temp = float ( input ( " enter temp in °F "))
           Result = fahrenheit_to_kelvin(fahrenheit_temp)
           print(f"{fahrenheit_temp}°F = {Result:.2f} K ")


        elif choice == 6 :
           kelvin_temp = float ( input ( "enter temp in K "))
           Result = kelvin_to_fahrenheit(kelvin_temp)
           print(f"{kelvin_temp} K = {Result:.2f}°F " )

    
        elif choice >= 7 :
            print("👋 Thank you for using the Temperature Converter!")
            break
        

        else:
            print("❌ Invalid choice! Please try again.")

main()
           
        



