# What is an Iteration

# Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

# Example
num = [1,2,3]

for i in num:
    print(i)

# What is Iterator

# An Iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory

# Example
L = [x for x in range(1,10000)]

#for i in L:
    #print(i*2)
    
import sys

print(sys.getsizeof(L)/64)

x = range(1,10000000000)

#for i in x:
    #print(i*2)
    
print(sys.getsizeof(x)/64)

# What is Iterable

# Iterable is an object, which one can iterate over

# It generates an Iterator when passed to iter() method.

# Example

L = [1,2,3]
print(type(L))

# L is an iterable
print(type(iter(L)))

# iter(L) --> iterator

# Point to remember
# Every Iterator is also and Iterable
# Not all Iterables are Iterators

# Trick
# Every Iterable has an iter function
# Every Iterator has both iter function as well as a next function
#********************
a = 2
print(a)

#for i in a:
    #print(i)
    
print(dir(a))
#********************
T = {1:2,3:4}
print(dir(T))
#********************
L = [1,2,3]

# L is not an iterator
iter_L = iter(L)
print(dir(iter_L))
# iter_L is an iterator

# **************Understanding how for loop works**************
num = [1,2,3]

for i in num:
    print(i)
#*********************
num = [1,2,3]

# fetch the iterator
iter_num = iter(num)

# step2 --> next
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
# print(next(iter_num))

# *****************Making our own for loop
def mera_khudka_for_loop(iterable):
    
    iterator = iter(iterable)
    
    while True:
        
        try:
            print(next(iterator))
        except StopIteration:
            break           

a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}

mera_khudka_for_loop(e)

# A confusing point

num = [1,2,3]
iter_obj = iter(num)

print(id(iter_obj),'Address of iterator 1')

iter_obj2 = iter(iter_obj)
print(id(iter_obj2),'Address of iterator 2')

# Let's create our own range() function

class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_range_iterator(self)

class mera_range_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
            
        current = self.iterable.start
        self.iterable.start+=1
        return current

x = mera_range(1,11)
print(type(x))
print(iter(x))