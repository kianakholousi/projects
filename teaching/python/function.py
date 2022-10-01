#Python built-in functions
import random
import math
a = abs(-23)
maximum = max([2,5,7,6])
max2 = max(2,5,9,7)
p = pow(2,3)
p2 = 2**3
# r = round(1.83)
r = int(1.67)
r2 = round(1.67,1)
rand = random.randint(2,5)

# print(max(3,5))
# print(rand)
# print(a,maximum,max2,p,r,r2)
# print(help(max))

def function_name():
    print("this is a function")
    print("line2")
    
def func(name):
    print("hello " + str(name))   

def multiply(x,y):
    result = x*y
    return result
    print("after return statement") #statements after return dont execute
    
#=============== 
function_name()
func(2.54) 
print(multiply.__doc__) #use to see function documentation
print(multiply(3,4))

# pass by value
def increment_func(x):
    x+=1
    return x
x=1
print(increment_func(x))
print(x)
  
string = "spam"
def test(string):
    string ="eggs"
    print("string inside the function is: ",string)
test(string)    
print("string outside the fuction is: ",string)

myList =[10,20,30,40]   
def test2():
    list.append(50)
    myList =[10,20,30,40,50]
    print("func list: ",myList)
test2()
print(myList)    
# newfunc() #error cant call function before definition
def newfunc():
    print("1")
    
newfunc()  


def dev(a,b=1):
    if(b==0):
        print("not possible")
    elif(a==0):
        return 0
    else: 
        return a,b,a/b 
    
print(dev(4,3))
         
#lambda 
# print(x(4,3))
x = lambda a,b : a * b
print(x(2,4))
print(x(5,3))

# map & filter
nums = [11,22,33,44,55]
result = list(map(lambda x : x+5 ,nums))
res = list(filter(lambda x:x%2==0 ,nums))
print(result)
print(res)

# generator
def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
    print(i, end=' ')

def numbers(x):
    for i in range(x):
        if i%2 ==0:
            yield i

print(list(numbers(20)))

# decorator
def decor(func):
    def wrap():
        print("=============")
        func()
        print("=============")
    return wrap

@decor 
def print_txt():
    print("Hello World!")        

print_txt = decor(print_txt)
print_txt()

# python recursion
def factorial(x):
    if x==1:      #base case
        return 1
    else:
        return x * factorial(x-1)    
print(factorial(50))

# indirect recursion
def is_even(x):
    if x%2==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not  is_even(x)

print(is_odd(23))
print(is_even(13))

def function(first_arg,*b):
    print(first_arg, end=" ")
    print(b)
    print(sum(b)+first_arg)
    
function()
function(1)
function(1,2)    
function(1,2,3)
function(1,2,3,4,5)  

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    
func(2,3,4,5,6,car="bmw",RPM=800)

