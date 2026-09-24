
try:
    num1 = input("Give me a number: ")
    float1 = float(num1)
    
    if float1.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass