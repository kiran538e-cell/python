#Set unique collection of set,data structure with python.
numbers = {1,2,3,5,6,7} 
s2 = {3,4,6,7,9,8,0}
print("Set Program Ended")                          #collection of unique values {} remove automatically remove duplicate values.
print(numbers)                                      #changable
print(len(numbers))
numbers.add(10)
print(numbers)
numbers.remove(2)
print(numbers)
print(5 in numbers)      #return boolean result check presence
print(7 in numbers)
print(len(numbers))
print(numbers)
print("Union:" , numbers.union(s2))
print("Intersection:" , s2.intersection(numbers))
print("Set Program Ended")
