#  Python Program to print n prime number
import math
Number = int(input(" Please Enter any Number: "))
print("Prime numbers between", 1, "and", Number, "are:")
n=1
# using for
for num in range(1, Number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# using while
while(n <= Number):
    count = 0
    i = 2
    while(i <= math.sqrt(n)):
        if(n % i == 0):
            count = count + 1
            break
        i += 1
    if (count == 0 and n != 1):
        print("%4d" %n ,end="")
    n = n  + 1           