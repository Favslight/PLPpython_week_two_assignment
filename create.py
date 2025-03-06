my_list = []
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("after append:", my_list)

my_list.insert(1, 15)

sec_list = [50, 60, 70]

my_list.extend(sec_list)
print("After extend:", my_list)

my_list.pop(-1)
print(my_list)

my_list.sort()
print(my_list)

index_of_30 = my_list.index(30)

print(index_of_30)