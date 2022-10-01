# scope
t=20 
# x=3   
print("outside1: ",t)
def func1(x,y):
    z=2
    t=10
    print("inside: ",t)
    # print(x+z)
    # print(x,y,z)

t=20
print("outside1: ",t)
func1(1,2)
# print(x,y,z)    #error variables defined in function scope
print("outside2: ",t)

#==============================
x="global"
def outer():
    x = "local"
    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("outside of function:",x)
#==========================
c = 0 # global variable
def add():
    global c
    c = 2 
    print("Inside add():", c)
add()
print("In main:", c)
#==============================
def fouter():
    x = 20 #local
    def finner():
        global x
        x = 25 #global
        print("inside finner:",x)
    print("Before calling finner: ", x)
    print("Calling finner now")
    finner()
    print("After calling finner: ", x)
fouter()
print("x in main: ", x)
#=============================
def fun():
    var1 = 10
    
    def fun2():
        nonlocal var1
        var1 = var1 + 10
        print(var1)
 
    fun2()
fun()
