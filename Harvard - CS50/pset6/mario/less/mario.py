from cs50 import get_int

# prompt user for pyramid hight
height = get_int("Height: ")
while not (1 <= height <= 8):
    height = get_int("Height: ")

# print out pyramid layer by layer
for i in range(height):
    s = ""
    for j in range(height):
        if j < height - i - 1:
            s += " "
        else:
            s += "#"
    print(s)
