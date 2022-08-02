# generators are special functions in python
# that can be used to generate a sequence of values
# instead of returning the value from a function once
# we put the value into a memoery space using the yield keyword
# and then we can use the next() function to get the next value
# generators are fast compared to lists

from re import A


def cube(limit):
    for i in range(1,limit):
        yield i**3

# fibonacci series
def fib(limit):
    a,b = 0,1
    for i in range(limit):
        yield a
        a,b = b,a+b

# ex call
for c in cube(10):
    print(c)

for f in fib(15):
    print(f,end ='| ')

# wap to generate a list of even squares using generators

def even_squares(limit):
    for i in range(0,limit,2):
        yield i**2

for a in even_squares(20):
    print(a)

