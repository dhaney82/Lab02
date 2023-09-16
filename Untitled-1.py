# Lab02 Part 1

part1list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
resultpart1 = 1
for x in part1list:
    resultpart1 = resultpart1 * x
print("Multiplying all the numbers in this list together equals", resultpart1)

# Lab02 Part 2

part2list = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
resultpart2 = 0
for y in part2list:
    resultpart2 += y
print("Adding all the numbers in this list together equals", resultpart2)

# Lab 02 Part 3

part3list = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
resultpart3 = 0
for z in part3list:
    if z % 2 ==0:
        resultpart3 += z
print("Adding together only the even numbers in this list equals", resultpart3) 