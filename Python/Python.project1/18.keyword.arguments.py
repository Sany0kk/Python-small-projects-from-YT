# keyword arguments = arguments preceded by an identifier when we pass them to a funtion
#                     The order of the arguments doesnt matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Bro",middle="Dude",first="Code")