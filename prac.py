my_list=[1,5,2,8,9,3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.remove(5)
print(my_list)
my_list[3]="hello"
print(my_list)
my_list.insert(1,"hi")
print(my_list)

my_dict={"name":"johns","age":25,"city":"mumbai"}
print(my_dict)
my_dict["year"]=2024
print(my_dict)
del my_dict["age"]
print(my_dict)
my_dict["city"]="banglore"
print(my_dict)

my_set={1,2,3,4,5,9}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(4)
print(my_set)

my_tuple=(1,2,1,2,4,4,3,3,7,6,8,"mahesh")
print(my_tuple.count(1))
print(my_tuple)
print(my_tuple[3])