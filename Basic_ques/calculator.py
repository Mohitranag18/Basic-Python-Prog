choice = input("Select the Operation you want to do:- \n A. addition \n B. subtraction \n C. multiply \n D. divide \n Select from A, B, C or D: \n")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if(choice == "A" or choice == "a"):
    print("addition is = ",num1 + num2)
elif(choice == "B" or choice == "b"):
    print("subtraction is = ",num1 - num2)
elif(choice == "C" or choice == "c"):
    print("multiplication is = ",num1 * num2)
elif(choice == "D" or choice == "d"):
    print("division is = ",num1 / num2)

