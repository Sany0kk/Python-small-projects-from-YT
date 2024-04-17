# logical operators (and,or,not)
# 'or' - True and False = True
# 'and' - True and False = False
# 'not' - reverses True value to False
temp = int(input("What is the temperature outside?: "))

if  temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp >30:
    print("the temperature is bad today!")
    print("stay inside!")
