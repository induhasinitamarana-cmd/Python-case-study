# Case Study 7: Hollow Diamond Pattern
size = 7

if size <= 0 or size % 2 == 0:
    print("Enter a positive odd size.")
else:
    middle = size // 2
    for row in range(size):
        distance = abs(middle - row)
        leading_spaces = distance
        width = size - (2 * distance)

        print(" " * leading_spaces, end="")
        if width == 1:
            print("*")
        else:
            print("*" + " " * (width - 2) + "*")
