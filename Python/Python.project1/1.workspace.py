


print("******* Temperature converion *******\n")
print("F = Fahrenheit\n")
print("C = Celsius\n")
unit = input("What unit would you like to convert to: ")

if unit.lower() == 'f':
    print("Enter the temperature in Celsius: ")
    temp = float(input())

    temp = (1.8 * temp) + 32.0

    print(f"Temperature is: {temp} F \n")

elif unit.lower() == 'c':
    print("Enter the temperature in Fahrenheit: ")
    temp = input()
 
    temp = (temp - 32) / 1.8
    print(f"Temperature is: {temp} C \n")

else:
    print("Please enter in only C or F \n")

