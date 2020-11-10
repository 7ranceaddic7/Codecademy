convert_temp = 0

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    print(str(f_temp)+ " degrees Fahrenheit equals " +str(c_temp)+ " degrees Celsius.")

def c_to_f(c_temp):
    f_temp = (c_temp * 9/5) + 32
    print(str(c_temp) + " degrees Celsius equals " +str(f_temp) + " degrees Fahrenheit.")

def ask_user():
    response = ''
    print("What scale do you want to convert?")
    while response.lower() not in {"f", "c"}:
        response = input("Please enter (F)ahrenheit or (C)elsius: ")
        if  response.lower() == "f":
            convert_temp = input("What temperature Fahrenheit do you want to convert to Celsius? ")
            f_to_c(float(convert_temp))
        elif response.lower() == "c":
            convert_temp = input("What temperature Celsius do you want to convert to Fahrenheit? ")
            c_to_f(float(convert_temp))

ask_user()
