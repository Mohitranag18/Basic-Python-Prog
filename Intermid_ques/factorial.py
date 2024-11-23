num = int(input("Enter the number to find Factorial"))
fact = 1
while(num >= 1):
    fact *= num
    num -= 1

print(fact)