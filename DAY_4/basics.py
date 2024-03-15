# Day 4(07-03-2024)
# Match cases, loops(for, while), fuctions, exceptional handling

# Match cases
a = int(input("ENter the number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case _: #default cases
        print("No match found")

# for loop
for i in range(5):
    print(i)


# Can work with list, tupel
a = [45,5,6,7,89]
a = "Shraddha"
print("Printing set")
for i in a:
    print(i)

# while loop
i = 0
while(i<3):
    print(i)
    i = i + 1


# functions
def greet():
    print("Good morning")

def greet1(name):
    # f strings
    st = f"hi mam {name}"
    print(st)
    print(name)

def avgerage(a, b):
    return (a+b) /2

greet()
greet1("Vaibhav Goyal")
print(avgerage(2,3))


# Exceptional handling
# we use when there is the possibility of error in our program
try:
    a = int(input("Enter your number: "))
    print(a + 3)
except Exception as e:
    print("some error occured: ", e)
except:
    print("Some error occured")
