# Just like in maths these two methods work here

s1 = {2,4,5,6}
s2 = {1,3,4,5}
s3 = s1.union(s2)
print(f"The set 1 is {s1} set 2 is : {s2}, and their union is: {s3}")

# Intersection is here
s4 = s1.intersection(s2)
print(f"The set 1 is {s1} set 2 is : {s2}, and their union is: {s4}")

#Checking fsor the subset
print({2,4}.issubset(s1)) #return True
print({3,9}.issubset(s2)) #return False

# Checking whether s1 is super subset of ....
print(s1.issuperset({5,6})) #if yes return True else False