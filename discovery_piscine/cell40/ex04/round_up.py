
import math

try:
    user_input = input("Give me a number: ")
    num = float(user_input)
    print(math.ceil(num))
except ValueError:
    pass