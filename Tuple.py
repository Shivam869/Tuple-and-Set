my_tuple=()
print(my_tuple)
mytuple=(1,2,3)
print(mytuple)
my_tuple=(1,"hello",3.14)
print(my_tuple)
my_tuple=("mouse",(1,2,3),(7,8,9))
print(my_tuple)
my_tuple=(1,2,3,4,5,6,7,8,9,0)
print(my_tuple[0])
print(my_tuple[5])
my_tuple=(1,(2,3,4),(5,6,7,8))
print(my_tuple[0],[2])
print(my_tuple[1],[1])
print("Sliced:",my_tuple[1:4])
for letter in my_tuple:
    print("Hello",letter)