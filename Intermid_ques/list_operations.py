user_list = list(map(int, (input("Enter list of number with space seperated: ").split())))

largest = max(user_list)
smallest = min(user_list)
average = sum(user_list) / len(user_list)


print("List = ", user_list)
print("Largest = ", largest)
print("Smallest = ", smallest)
print("Sum = ", sum(user_list))
print("Average = ", average)