#condition
age = int(input("pleease enter yout age:"))
if age<13:
    print("child")
if age>=13 and age<20:
    print("teenage")
if age>=20:
    print("adult")
    
# =============
x,y = float(input()),float(input())
if x==y:
    print("x and y are equal")
else:
    if x<y:
        print("y is greater than x")
#     else:
#         print("x is greater than y")    
# #================= 
x=4 #5
if(x>=5):
    print("x>=5")
elif(x<=5):
    print("x<=5")
else:
    print("x=5")      
# #================= 
import math
a=int(input("x^2 constant: "))
b=int(input("x constant: "))
c=int(input("constant: "))
if a==0:
    print("x^2 cant be 0 ")
else:
    d= b*b -4*a*c
    if(d<0):
        print("no real roots")
    elif(d==0):
        root = -b / (2*a)
        print("double root is",root)    
    else:
        root1= -b +math.sqrt(d) / (2*a) 
        root2= -b +math.sqrt(d) / (2*a)
        print("roots: ",root1,root2)    
#    divide by 0  
x=1
if x>0 :
    pass
#==============================================================================================
letter = input("Enter a letter of the alphabet: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("its a vowel")
elif letter=="y":
    print("sometimes consonant and some times not")
else:
    print("its a consonant")
# special case y => elif
# ======================
nside = input("enter the number of sides(3-10): ")
if nside.isdigit():
    nside = int(nside)
    name =""
    if nside==3:
        name = "triangle"
    if nside==4:
        name = "quadrilateral"
    if nside==5:
        name = "pentagon"        
    if nside==6:
        name = "hexagon"
    if nside==7:
        name = "heptagon"                
    if nside==8:
        name = "octagon"
    if nside==9:
        name = "nonagon"    
    if nside==10:
        name = "decagon"    
    if name=="":
        print("that number of sides is not supported by this program")
    else:
        print("that is a",name)        
else:    
    print("enter a numeric value")    