"""
Name: Jeron Amory
Email: j.amory268@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

"""
A
"""
print("A:")
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1, 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

a.append(2)

"""
B
"""
def remove_all(el, lst):
    """Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
print("B:")
for x in a:
	
	if x == 2:
		a.remove(2)
print(a)
	

"""
C
"""
a.append(4)
print("C:")
def add_this_many(x, y, lst):
    """ Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
for z in a:
	if z == 4:
		a.append(9)
print(a)
add_this_many(4, 9, a)

"""
D 
"""
print("D:")
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]


"""
E 

print("E:")
def reverse(lst):
 Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]

for i in a[::-1]:
	print(i)
"""

	
"""
F 
"""
print("F:")
def rotate(lst, k):
	x = a[k:] + a[:k]
print(a)


"""
H
"""
print("H:")
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
superbowls['peyton manning'] = 1
superbowls['joe flacco'] = 1

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe montana': 4, 'peyton manning': 1, 'tom brady': 3, ('eli manning', 'giants'): 2, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {'tom brady': 3, 3: 'cat', ('eli manning', 'giants'): 2, 'joe montana': 4, 'peyton manning': 1, 'joe flacco': 1}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'tom brady': 3, 3: 'cat', ('eli manning', 'giants'): 5, 'joe montana': 4, 'peyton manning': 1, 'joe flacco': 1}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'peyton manning': 1, 3: 'cat', ('steelers', '49ers'): 11, 'tom brady': 3, ('eli manning', 'giants'): 5, 'joe montana': 4, 'joe flacco': 1}


"""
I 
"""
print("I:")
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
def replace_all(d, x, y):
	for key in d.keys():
		if key == x:
			d[key] = 7
replace_all(d, 4, 7)
print(d)


"""
J 
"""
print("J:")
def rm(d, x):
	for key in d.keys():
		if d[key] == x:
			del d[key]
	
rm(d, 4)
print(d)
