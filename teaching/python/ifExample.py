x= int(input())
if(x>0):
    if(x%2==0):
        print("positive Even")
    else:
         print("positive Odd") 
elif(x<0):
    if(x%2==0):
        print("Negative Even")
    else:
         print("Negative Odd")  
else:
    print("Zero") 
number1=int(input())
if(number1>0):
    msg1="positive"
else:
    msg1="Negative"
if(number1%2==0):
    msg2=" Even"
else:
    msg2=" Odd"
print(msg1+msg2)
#======================   
n=int(input())
for i in range(1,n+1):
    if(i%2==0):
        print(i,end=" ")
# ================
zip_code = input()
if len(zip_code) == 11 and zip_code.isdigit() == True:
        print("%s is a valid Zip Code!" %(zip_code))
else:
        print("%s is not a valid Zip Code!" %(zip_code))        
#===================================
num1 = (input("Please Enter Number1: "))
operator = input("Please Enter the operator(+ - * /): ")
num2 = (input("Please Enter Number2: "))
if num1.isdigit() and num1.isdigit():  
    num1 = int(num1)   
    num2 = int(num2)   
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":     
        result = num1 / num2
    else:
        result = "The operator is not valid!"
    print(result)                
else:
    print("Something went wrong!")


    
    