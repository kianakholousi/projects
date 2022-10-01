tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34.2, True, 40, "day") #mixed datatypes
tuple5 = "apple", "banana", "cherry", "apple", "cherry",
tuple6 = tuple(("apple", "banana", "cherry"))
my_tuple = () #empty tuple 

print(my_tuple)
print(len(tuple4))
print(type(my_tuple))

#tuple with one element
thistuple = ("apple")
print(type(thistuple))
thistuple = ("apple",)
print(type(thistuple))
# Parentheses is optional
thistuple = "apple",
print(type(thistuple))

# operation
print(tuple1+tuple2) #concat 
print(tuple3*3)
print((1,23,49,)+(7,6,53,))
print((2,5,6,)*2)

# #indexing
tuple4 = ("abc", 34.2, True, 40, "day")
print(tuple4[2])
print(tuple4[-1])
print(tuple4[len(tuple4)-1])

# #iteration
tuple5 = "apple", "banana", "cherry", "apple", "cherry",
for i in tuple5:
    print("i love "+i)
    
for i in range(len(tuple5)):
    print(tuple5[i])

#slicing
tuple4 = ("abc", 34.2, True, 40, "day")
print(tuple4[1:3])
print(tuple4[:3])
print(tuple4[2:])   
print(tuple4[:])
print(tuple4[::2]) 
print(tuple4[-4:-1]) 
print(tuple4[-1:-4:-1]) 
print(tuple4[::-1])#reverse

# immutable
tuple5 = "apple", "banana", "cherry", "apple", "cherry",
#cant access/change/delete a tuple item
# tuple5[2]="peach" 
# del tuple5[0]

#pass by value
def func1(t):
    t = t * 2
    print("inside func",t)

t = (1, 2, 3)
print("before func",t)
func1(t)
print("after func",t)


#packing
a_tuple = 3, 4.6, "dog"
# print(a_tuple)

# tuple unpacking 
a, b,c = a_tuple
# print(a,b)
    
# nested
t = ((1, 2,3), (3, 4), (("a", "b", "c"), 3.4))
# print(t)

for j in t:
    for k in j:
        print(k,end = " ")
    print()

# method
thisTuple=("python","c#","c++","c","java",2,22,32,2)
print(thisTuple.count("c"))
print(thisTuple.count(5))
print(thisTuple.index("c"))
# print(thisTuple.index(5)) #error
tup=12,43,100,13,92
# tup="bye","goodbye","hello","hi","hey" #try min/max function with string filled tuple
print(type(tup))
print(len(tup))
print(min(tup))
print(max(tup))
del tup
# print(tup) #name error

# # in keyword
thisTuple=("python","c#","c++","c","java",2,22,32,2)
print("c" in thisTuple)
if 2 in thisTuple:
    print("yes")
else:
    print("no")    
   
# args is a tuple 
def func(*args):
    print(args)
    print(sum(args))
    print(type(args))
   
func()   
func(45)    
func(1,2,3,4)