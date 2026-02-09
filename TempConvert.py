#TempConvert.py
#Name: Talia Astorino
#Date: 02/08/2026
#Purpose: Using boolean logic, conditional statements, loops, and program flow control.

def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float((input("Enter a temeperature in fahrenheit. ")))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((tempF - 32) * 5/9, 1)
  #Output converted temperature.
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
