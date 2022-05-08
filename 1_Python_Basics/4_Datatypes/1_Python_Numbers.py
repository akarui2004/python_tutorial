# Python number types: int, float, complex
a = 5
print(a, "is of type", type(a))
# Result
# 5 is of type <class 'int'>

a = 2.9
print(a, "is of type", type(a))
# Result
# 2.9 is of type <class 'float'>

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
# Result
# (1+2j) is complex number? True