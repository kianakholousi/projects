#counting
start = int(input("enter start number: "))
end = int(input("enter end number: "))
# odd numbers
while True:
    if end<start:
        break
    else:
        if start%2==1:
            print(start, end=" ")
        start+=1
# #even  
while end>start:
    if start%3==0:
        print(start)
    if start%2==0:
        print("even",start)
    start+=1
    
# sum and total
x=0
sum=0  
count=0
while x!=-1:
    x=int(input("new number or -1 to exit: "))
    sum+=x       #sum = sum + x
    count+=1 
print("sum=",sum) 
print("you enterd a total of "+str(count)+" numbers") 
       