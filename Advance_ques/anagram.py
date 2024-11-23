def is_anagram(first_str, second_str):
    if len(first_str) != len(second_str):
        return False
    flag = 0
    for i in first_str:
        for j in second_str:
            if i == j:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            return False
    return True
    
first_str = input("Enter the first string : ")
second_str = input("Enter the second string : ")
first = first_str.replace(" ","")
second = second_str.replace(" ","")

if is_anagram(first, second): 
    print("String 1 and String 2 are Anagram")
else:
    print("String 1 and String 2 are NOT Anagram")