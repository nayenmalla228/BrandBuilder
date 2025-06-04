#create a dictionary ,different values rakhni string,int,float and list and 
#update garera insert name=milan
#create a set ,add two element
#set banayera union ra intersection garni

dict2={
    "nam":"nayen",
    "age":23,
    "weight":60.5,
}
print(dict2)

dict2.update({"name":"milan"}) #update garera name milan rakheko
print(dict2)

set2={2,3,4,5,6}
set3={4,5,9}

set_union=set2.union(set3) #union
print(set_union)

set_intersection=set2.intersection(set3) #intersection
print(set_intersection)

set_diff=set2.difference(set3) #difference
print(set_diff)
