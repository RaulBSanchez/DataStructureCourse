'''
def print_items(n):
	for i in range(n):
		print(i)



print_items(10)

o(n) this ran n times, n operations


def print_items(n):
	for i in range(n):
		print(i)

	for j in range(n):
		print(j)

print_items(10)

# this ran n + n times =  2n == 0(2n)  but you drop the constant so 



def print_items(n):
	for i in range(n):
		for j in range(n):
			print(i,j)

print_items(10)

# this is ran n * n times, so this is n squared o(n^2)
# a lot less efficent from a time complexity stand point




#drop non dominants

def print_items(n):
	for i in range(n):
		for j in range(n):
			print(i,j)
	for k in range(n):
		print(k)


print_items(10)


# this would be n^2 + n but if the number would get huge, you can drop n because of the rate it grows




#O(1) only one operation, constant time

def add_items(n):
	return n + n

add_items(10)
'''


my_list = [11, 3, 23, 7]

my_list.append(17)

# on lest if you pop or append to end, its O(1) but anything to beginning in terms of adding/removing its O(n)
