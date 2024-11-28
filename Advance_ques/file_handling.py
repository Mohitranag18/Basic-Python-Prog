with open("test.txt", "w") as file:
    file.write("hey, this is mohit rana. \nthis is a test file.\n")
    print("data entered successfully.")


with open("test.txt") as file:
    print(file.read())

with open("test.txt", "a") as file:
    file.write("this is 3rd line ")
    print("file append successfullly")

