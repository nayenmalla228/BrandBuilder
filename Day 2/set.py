#sets

set1={1,2,2,3,4}
print(type(set1))
set1.add(5) #add element to set
print(set1)

set1.remove(2) #remove element from set
print(set1)

set1.clear() #clear all elements from set
print(set1)

set2={1,2,3,4,5,6}
set3={4,5,6,7,8}

#union
set_union=set2.union(set3)
print(set_union)

#intersection

set_intersection=set2.intersection(set3)
print(set_intersection)