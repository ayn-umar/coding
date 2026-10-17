for i in range(1,8,2):
    print(i)

print("A Loop")
for j in range(1,10,4):
  print(j)



print("B Loop")
for i in range(2):
  for j in range(15):
        print("i is", i, "j is", j)

print("C Loop")
i=2
while i<10:
        print(i)
        i=i+1

number = int(input("Enter a number: "))
for i in range(1,11):
     print(number, "x", i, "=", number*i)
