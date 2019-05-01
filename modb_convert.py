# File: convert.py
# A program to convert Celsius temps to Fahrenheit
# Modified 05/01/19
# By: Justin Mantis

def main():
  print("Convert Celsius to Fahrenheit")
  print("Celsius temperature\tFahrenheit Equivalent")
  for currentCelsiusTemperature in range(0,101,10):
    fahrenheitTemperatureEquvalent = ( 9 / 5 ) *currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t", \
      format( fahrenheitTemperatureEqucalent, ".1f") )
  for i in range(5):
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
  input("Press the <Enter> to quit.")
main()
