# Day 4(07-03-2024)
# file io

# File in python
s = "Shraddha is the good girl"

# no need to close it with with

# Writing in the file #1
# in write mode if we write then it will be erase
with open("test.txt", "w") as f:
    f.write(s)

# 2
fp = open("test.txt", "w")
fp.write(s)
fp.close()

# Reading the file
with open("test.txt", "r") as f:
    sp = f.read()
    print(sp)


# appending in the file
# append will add after it
with open("test.txt", "a") as f:
    f.write("Hello is the ")
