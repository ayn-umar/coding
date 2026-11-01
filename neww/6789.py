names = ["Alice", "Bob", "Charlie" , "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
print(names)
print("First name:", names[0])

print("Length of names list:", len(names))

#append 
names.append("Kevin")
names.append("Laura")
print("After appending Kevin and Laura:", names)

names.pop(4)  # This will remove the element at index 4 from the list
print("After popping the element at index 4:", names)


print("sorted names list:", sorted(names))
print("reversed names list:", list(reversed(names)))


print("slicing names list:", names[2:5])



#dictionary

students = { "name": "ayan" , "age": 16, "city": "Islamabad" }
print("Student dictionary:", students)
students.pop("age")
print("After popping 'age' key:", students)
