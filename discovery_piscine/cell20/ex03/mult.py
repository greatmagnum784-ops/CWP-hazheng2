input1 = int(input("Enter the first number:\n"))
input2 = int(input("Enter the second number:\n"))

ans = input1 * input2
print(f"{input1} x {input2} = {ans}")
if ans > 0 :
	print("The result is positive")
elif ans < 0:
	print("The result is negative")
else:
	print("The result is positive and negative.")