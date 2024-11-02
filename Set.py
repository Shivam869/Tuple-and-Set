my_set={1,2,2,3,3,3,4,4,4,4,4}
print("Set:",my_set)
my_set.add(5)
print("Set:",my_set)
set1=(my_set)
set2={6,7,8,9,0,4,2}
print("\n Set 1",set1)
print("Set 2",set2)
print("difference")
print(set1.difference(set2))
print("Semetric Difference")
print(set1.symmetric_difference(set2))