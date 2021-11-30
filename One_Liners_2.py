# *********** 1. If - else *****************
"""

Generally, we use the following code to write conditional statements

if 3 < 2:
    variable = 21
else:
    variable = 42

It can be written as a one-liner as:"""

variable = 21 if 3 < 2 else 42

# ********** 2. if - elif - else *************

"""
x = 42
if x < 42:
    print('No')
elif x == 42:
    print('Yes')
else:
    print('Maybe')
"""

x = 42
print('No') if x < 42 else print('Yes') if x == 42 else print('Maybe')

# *********** 3. If without else ***************

"""
condition = True
if condition:
    print("Hi")
"""

condition = True

# Method 1:
if condition: print('Hi')

# Method 2:
print("Hi") if condition else None

# ************ 4. Function ****************

"""
def f(x):
    return "Hello " + x
    
Where x is a string value that will be concatenated with the defined String in f(x) "Hello "
So if x = '3' and f(x) is printed, then output is as:
        
        Hello 3
        
"""

f = lambda x: "Hello " + x

# ************ 5. List Comprehension / looped list **************

"""
squares = []
for i in range(10):
    squares.append(i ** 2)
"""

squares = [i ** 2 for i in range(10)]

# ************ 6. Loop with if **************

"""
squares2 = []
for i in range(10):
    if i%2 == 0:
        squares2.append(i**2)
"""

squares2 = [i ** 2 for i in range(10) if i % 2 == 0]

# ************* 7. Loop with if - else **************

"""
squares3 = []
for i in range(10):
    if i%2 == 0:
        squares3.append(i**2)
    else:
        squares3.append(False)
"""

squares3 = [i ** 2 if i % 2 == 0 else False for i in range(10)]

# ************** 8. While loop with if else **************

"""
c = 0
while c < 10:
    if c != 5:
        print(c)
    else:
        print("FIVE")
    c += 1
"""

c = 0
while c < 10: c += 1; print(c) if c != 5 else print("FIVE")

# ************** 9. Multiple assignment **************

"""
a = "ONE"
b = 2
c = 3 + 4j
"""

a, b, c = "ONE", 2, 3 + 4j

# ************** 10. Write String in a file **************

"""
text = "Hello This is Python Programming"
filename = "Welcome.txt"
f = open(filename, "a")
f.write(text)
f.close()
"""

text = "Hello This is Python Programming"
filename = "Welcome.txt"
print(text, file=open(filename, "a"))

# ************** 11. Fibonacci Sequence **************

"""
def fib(x):
    if x <= 2:
        return 1
    return fib(x - 1) + fib(x - 2)
"""

fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)

# ************** 12. Nested for loop **************

"""
i = [1,2,3,4]
j = ['a','b','c']
for x in i:
    for y in j:
        print(x, y)
"""

i = [1, 2, 3, 4]
j = ['a', 'b', 'c']
[print(x, y) for x in i for y in j]

# ************** 13. Print without a new line **************

"""
for i in range(1, 5):
    print(i, end=' ')
"""

print(*range(1, 5))

# ************** 14. Class **************

"""
class School():
    fun = []
"""

School = type('School', (object,), {'fun': {}})