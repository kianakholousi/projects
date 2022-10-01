#avg
n=int(input("how many numbers do you have? "))
sum=0
count=0
for i in range(1000):#starts from 0 dosen't inculde n
    x =float(input("enter "+str(i+1)+"th number:"))
    if x ==-1:
        break
    sum+=x
    count+=1   #count = count+1 
print("avrage=",sum/count)    
        
# printing odd/even numbers
n=int(input("Enter n: "))
for i in range(0,n+1,3): 
    if i%2==0:
        continue
    print(i,end =" ")

#fibonacci
n = int(input("enter n: "))
f1=0
f2=1
print(f2,end=" ")
for k in range(1,n):
     f_new = f1 +f2 
     print(f_new,end=" ")
     f1=f2 
     f2 = f_new

# square
for i in range(9):
    if i==0 or i==8:
        x="*********"
    else:
        x="*       *"    
    print(x)    

#palindrome String
line = input("Enter a String: ")
is_palindrome = True
for i in range(0,len(line)//2):
    if line[i] != line[len(line)-i-1]:
        is_palindrome = False
if is_palindrome:
    print(line,"is a palindrome")   
else:
    print(line,"is not a palindrome")       
  
#multiplication table
Min=1
Max=10
for i in range(Min,Max+1):
    for j in range(Min,Max+1):
        print(i*j,end="\t")
    print()    
            
      