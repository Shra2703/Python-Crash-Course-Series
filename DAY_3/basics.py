# Day 3(06-03-2024)
# Lists, tuples, sets, dictionares


# Lists (are mutable)
# Lists can have hetrogeneous methods
l1 = [1,2,34,56,"harry"]
print(l1)
l1[0] = "Shraddha"
print(l1)

# Lists method
l2 = [89,76,34,2,90]
l2.sort()
print(l2)
l2.append(900)
print(l2)
l2.pop()
print(l2)
l2.extend([90,89,78])
print(l2)

# Tuples (imuatable)
t = (1,23,45,67)

print(t.index(1))
print(t[2])
# t[2] = 89 gives error because it is immutable

# Sets (contains only unique element)
# performs all set operations
# can't access it like the lists because elements are the random posotion

s = {23,34,5,5,90,90}
s1 = set() #empty set
print(s)
print(s.pop()) #poped out the random element
print(s)
s.add(899)
print(s)

# dictionaries it is a key value pair
d = {} #empty set
print(type(d))

d1 = {"good" : "Something ", "fetch": 56}
print(d1["fetch"]) #fetching the data

d1[900] = "priyanka" #adding new key
print(d1)

print(d1.get("Hello moto")) #no error if no key is present but if [] notation then gives error

print(d1.keys()) #getting keys
print(d1.values()) #getting only values
print(d1.items()) #getting both
