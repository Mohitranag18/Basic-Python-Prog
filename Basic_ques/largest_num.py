num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = num1
if(num2 > num1 and num2 > num3):
    print("Second number is Largest")
elif(num3 > num1 and num2):
    print("Third number is Largest")
else:
    print("First number is Largest")