import random
Number = random.randint(1,100)
print(Number)
def guess_num(Number):
    Number = Number
    Entered_num = int(input("Enter Number b/w 1 to 100: "))
    if Entered_num == Number:
        print("Congratulations, you have entered the correct number.\n")
    elif Entered_num > Number + 10:
        print("Too High, try again:\n")
        guess_num(Number)
    elif Entered_num < Number - 10:
        print("Too low, try again:\n")
        guess_num(Number)
    else:
        print("You are very close, try again: \n")
        guess_num(Number)

guess_num(Number)