# We can convert between different data types by using different type conversion functions like int(), float(), str()
f = float(5)
print(f)

i = int(10.6)
print(i)
i = int(-10.6)
print(i)

set = set([1,2,3])
print("Set data = ", set)
tuple = tuple(set)
print("Tuple data = ", tuple)

list = list('hello')
print("List [Hello] = ", list)

# To convert to dictionary, each element must be a pair
dict1 = dict([[1,2],[3,4]])
print(dict1)

dict2 = dict([(3,26),(4,44)])
print(dict2)