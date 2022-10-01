import modules
name = input("please enter your name:")
modules.greeting(name)

x = float(input("enter yur favorite number:"))
y = float(input("and another number:"))

sum = modules.add(x,y)
sub = modules.subtract(x,y)
multi = modules.multiply(x,y)
div = modules.divide(x,y)

print ("sum=%.2f, subtraction=%.2f, multiplication=%.2f, division=%.4f" %(sum,sub,multi,div))

# ====================
import math 
print("value of pi number:",math.pi)

from math import e
print("value of e number:",e)
print(math.pi)

from math import *
print(sqrt(100))
print(pi) 

import math as m
print(m.e)
#===============
import modules 
import modules 
import modules 
import importlib
importlib.reload(modules)

# =============
print(dir(modules))
print(dir())

# ============
import modules as m1
print(m1.Zero)