num1 = 987
num2 = 4.0
intex = int(num2)
print(int(num1/num2)) #this demo was showing int conversion of a float
print(num1/num2) 

# Comments!!!
# Comments are great for notating code, reminding us to do things, or even saving stuff we don't want to delete


print('MATH OPERATORS-', '\n')
# MATH operators!!!

# + add
add1 = 5 + 6
print('add',add1)

# - subtract
sub1 = 10-5
print('sub', sub1)

# * multiply
mult = 9 * 9
print('mult', mult)

# / divide
div = 7 / 2
print('div', div)

# // floor divide
floor_div = 7 // 2
print('floor divide', floor_div)

# % modulo
mod = 7 % 2
print('mod', mod)

# SPOILER ALERT!!!! modulo is commonly used for determining even or odd!   number % 2 == 0:
print(7%2) # odd example

print(6%2) # even example

# strings!!!!!  Strings are immuteable!!!
print('\nStrings-->\n')
string1 = 'abc'
string2 = '13234 + 234234 / we\'re fotlksndltlkj'
string3 = "another string we've come up with"

string4 = string3 + ' THIS IS MY LITERAL ' +string2  # This is an example of concatenation
print(string4)

f_string = f"this is num1 --> {num1} !!!" #this is an f string or formatted string example
print(f_string)

# LISTS!!!
print('\nLISTS!:\n')

some_list = [1234, 'string', True, False, 5.098]

print(some_list)

# lists are ordered, 0-indexed, dynamic

print(some_list[2])  # the index of a list gives us the value!
print(some_list[1].upper())

order_list = [0, 1, 2, 3, 4]
print(len(order_list))
print(order_list[3])

# FUNC VS METHOD EXAMPLE:   FUNC -->    functioncall(input)  vs item.method(input)

print('LIST methods:\n')

# .append() adds an item to the end of the list
print(order_list)
order_list.append(5)
print(order_list)

# .remove()  removes the FIRST OCCURENCE of a value from a list
order_list.remove(5)
print(order_list)

# .insert() inserts a value into the list at specified postion
order_list.insert(0, 10)
print(order_list)

# .pop() defaults to removing the last element from the list, but you can specify postion optionally and can save the value!
popped_value = order_list.pop(0)
print(popped_value)
print(order_list)


# Conditionals!!!
#  if /elif /else 
age = 78

if age == 16:
    print('SWEET')


if age < 18 :
    print('Just a baby!')
elif age > 64:
    print('Senior')
else:
    print('adult')


# Truth - tree!   (and      or)
    # T & T = True
    # T & F = False
    # F & F = False

    # T | T = True 
    # T | F = True
    # F | F = False

if age < 18 :
    print('Just a baby!')
elif age >= 18 and age < 65:
    print('adult')
else:
    print('senior')

if age > 9872394872:
    print('really really old')

print('15' == 15) # equal value but not type

names = ['Hassan', 'David', 'Tucker']

if "Tucker" in names:
    print('Tucker made it to class today!')

# LOOPS!

#range function:
# for x in range(5,10,2):
#     print(x)

# For loop
# syntax-->   for item in items:
for name in names:
    print(name)
    if name == "Tucker":
        print('Tucker made it to class today!---LOOP VERSION')
# index loop
for i in (range(len(names))):
    print(names[i], i)
# while loop

print('WHILE loop')
pointer = 0
while True:
    print(names[pointer])
    pointer += 1
    if pointer > 1:
        break

print('\n')
#incrementing / decrementing
counter = 0
for x in range(5):
    counter = counter + 1
    counter += 1
print(counter)


num_ex = 456
num_ex1 = 45234
num_ex2 = 45547

if num_ex % 2 == 0:
    print(f'Number is even!!! --> {num_ex}')
else:
    print(f"Number is odd-->{num_ex}")


def odds(num):
    if num % 2 ==0:
        print(f'Number is even!!! --> {num}')
    else:
        return 'odd'
odds(num_ex1)
odds(num_ex2)
odds(num_ex)























