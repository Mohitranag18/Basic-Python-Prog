def fibonachi(num):
    first = 0
    second = 1
    pointer = first + second
    print(first)
    print(second)
    while pointer <= num:
        print(pointer)
        first = second
        second = pointer
        pointer = first + second



num = int(input("Enter a number to find fibonachi series till that: "))

fibonachi(num)