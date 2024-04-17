# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Alex",21,"male")

print(student.count("Alex")) # counts how many "Alex" is there
print(student.index("male")) # shows the index of this variable(2)

for x in student:
    print(x)

if "Alex" in student:
    print("Alex is here! ")
