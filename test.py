import random

a = [1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)

# 2
a = [1,2,3,4,5]
print(a[3:0:-1])

# 3
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

# List
a = [12,23,33]
a[0] = 22

print(a)

# 3
fruit=['apple', 'banana', 'papaya', 'cherry']
print( random.shuffle(fruit))

# 4
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))

# 4
a = 'a','b'
print(type(a))