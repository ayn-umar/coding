#tuple
recipe_pasta = ("pasta", "tomato sauce", "cheese", "basil")
print(recipe_pasta)
print("using index of 3:", recipe_pasta[3])

#sets
numbers = {1, 2, 3, 4, 5 , 45,78,28,4,7,9,0,2,3,4,76,98,25}
numbers2 = {1, 2, 3, 4, 5 , 45,78,28,4,7,4,7,65,70,35,64,23,12,34,56,78,90}
print("data is", numbers)
numbers.add(12)
numbers.discard(4)
print("data is", numbers)


#union intersection difference symmetric difference
union = numbers.union(numbers2)
print("union is", union)
intersection = numbers.intersection(numbers2)
print("intersection is", intersection)

diff=numbers.difference(numbers2)
print("difference is", diff)
symm=numbers.symmetric_difference(numbers2)
print("symmetric difference is", symm)
