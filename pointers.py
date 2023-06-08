'''
num1 = 11
num2 = num1

print("Before num2 value is updated")
print("num1 value is", num1)
print("num2 value is", num2)

# this points to address in memory, they are stored in same address. 
print("num1 points to ", id(num1))
print("num2 points to ", id(num2))

'''

dict1 = {'value' : 1}
dict2 = dict1

print("Before value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("dict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))	

dict2['value'] = 22

print("dict2 now points to ", id(dict2))
print(dict1)
