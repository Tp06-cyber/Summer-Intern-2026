# 1) Repeat a tuple three times using the * operator
print("1) Repeat Tuple")
t = (1, 2, 3)
print("Original Tuple:", t)
print("Repeated Tuple:", t * 3)

print("\n-----------------------------")

# 2) Join three tuples using the + operator
print("2) Join Three Tuples")
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)
new_tuple = t1 + t2 + t3
print("Joined Tuple:", new_tuple)

print("\n-----------------------------")

# 3) Check whether an element exists in a tuple
print("3) Check Element in Tuple")
t = (10, 20, 30, 40, 50)
element = 30

if element in t:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")

print("\n-----------------------------")

# 4) Find total, highest, and lowest without using sum(), max(), min()
print("4) Total, Highest and Lowest")
t = (12, 5, 8, 20, 15)

total = 0
highest = t[0]
lowest = t[0]

for i in t:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

print("\n-----------------------------")

# 5) Filter tuple values greater than 10
print("5) Filter Tuple")
n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for i in n:
    if i > 10:
        filtered += (i,)

print("Filtered Tuple:", filtered)

print("\n-----------------------------")

# 6) Count elements in a set without using len()
print("6) Count Elements in Set")
s = {"cat", "dog", "bird", "fish"}

count = 0
for i in s:
    count += 1

print("Number of elements:", count)

print("\n-----------------------------")

# 7) Combine two sets
print("7) Union of Two Sets")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

union_set = s1 | s2
print("Combined Set:", union_set)

print("\n-----------------------------")

# 8) Find common elements in two sets
print("8) Intersection of Two Sets")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1 & s2
print("Common Elements:", common)

print("\n-----------------------------")

# 9) Find elements in either set but not in both
print("9) Symmetric Difference")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1 ^ s2
print("Elements in either set but not both:", result)