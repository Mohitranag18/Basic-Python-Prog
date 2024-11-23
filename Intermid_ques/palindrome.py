def is_palindrome(user_input):
    result = ""
    for char in user_input:
        if char.isalnum():
            result += char.lower()

    left = 0
    right = len(result) - 1

    while left < right:
        if result[left] != result[right]:
            return False
        left += 1
        right -= 1

    return True

user_input = input("Enter a string to check Palindrome or not:\n")
if is_palindrome(user_input):
    print("This is Palindrome")
else:
    print("This is not Palindrome")

# Short trick for check Palindrome
def is_palindrome_short(string):
    result = string.replace(" ", "").lower()
    return result == result[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")


if is_palindrome_short(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
