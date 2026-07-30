''' Methods of sets 
Note : Here in sets order doesn't matter we can't expect 
python to maintain order as we did '''

#length of sets can be find in thhis way 
set = {23,45,56,67,87,98,10} # Print 7 as its length if we add exixting elements len don't increase
print(len(set))
set.add(23) 
set.add(45)
print(len(set)) #still print 7 for above reason

#an element is removed using re ove method
set.remove(98)
print(f"The set is :{set} and the length of thr set is:{len(set)}")

# pop remove an arbitary element and clear clear the set
set.pop()
print(f"The set is :{set} and the length of thr set is:{len(set)}")
set.clear()
print(f"The set is :{set} and the length of thr set is:{len(set)}")

