x1,x2,x3 = float(input()),float(input()),float(input())
maxi=0
if(x1>x2):
    if(x1>x3):
        maxi = x1
if(x2>x1):
    if(x2>x3):
        maxi = x2
if x3>x1:
    if x3>x2:
        maxi = x3
print(maxi)  
          
   