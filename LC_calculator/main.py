# driver code 
from calculator import Calculator
c=Calculator()    
while True:
    print("""1. Add
2. Subtract
3. Multiply
4. AND
5. OR
6. XOR
7. Change in basis""")
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    # check if choice is a legal value
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))  
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        
        if choice == '1':
            print(num1, "+", num2, "=\n")
            if (num1>0 and num2>0): #when both numbers are posetive
                c.flag=1
                c.display(c.binaryToDecimal(c.add(abs(num1),abs(num2))))
            elif((num1*num2)<0): #one number is negetive
                c.flag=2  
                #Sum of different sign numbers = sign of the larger number*(larger number - smaller number) 
                if(abs(num1)>abs(num2)): 
                    c.display(int(num1/abs(num1))*(c.binaryToDecimal(c.subtract(abs(num1),abs(num2)))))
                else:
                    c.display(int(num2/abs(num2))*(c.binaryToDecimal(c.subtract(abs(num2),abs(num1)))))
            else:   #both numbers negative => -1*(sum of posetive)
                c.flag=1
                c.display(-abs(c.binaryToDecimal(c.add(abs(num1),abs(num2)))))
           
        elif choice == '2':
            print(num1, "-", num2, "=\n")
            if((num1>0 and num2<0) or (num1<0 and num2>0)): #a+b or -a-b => sign of a*(sum of positive)
                c.flag=1
                c.display(int(num1/abs(num1))*(c.binaryToDecimal(c.add(abs(num1),abs(num2)))))
            else:
                c.flag=2    
                if(abs(num1)>abs(num2)): #Sub = sign of the larger number*(larger number - smaller number)
                    c.display(int(num1/abs(num1))*(c.binaryToDecimal(c.subtract(abs(num1),abs(num2)))))
                else: #a-b => -sign of b
                    c.display(-int(num2/abs(num2))*(c.binaryToDecimal(c.subtract(abs(num2),abs(num1)))))
            
        elif choice == '3':
            c.flag=3
            print(num1, "*", num2, "=\n") 
            # a.b=abs(ab) (a,b>0 or a,b<0) / a.b=-abs(ab) (a or b <0)
            if((num1*num2)>0):
                c.display(c.binaryToDecimal(c.multiply(abs(num1),abs(num2))))
            else:
                c.display(-abs(c.binaryToDecimal(c.multiply(abs(num1),abs(num2)))))
                    
        elif choice == '4':
            c.flag=0
            print(num1, "And", num2, "=\n")
            c.display(c.binaryToDecimal(c.AND(abs(num1),abs(num2))))
            
        elif choice == '5':
            c.flag=0
            print(num1, "OR", num2, "=\n")
            c.display(c.binaryToDecimal(c.OR(abs(num1),abs(num2))))
            
        elif choice == '6':
            c.flag=0
            print(num1, "Xor", num2, "=\n")
            c.display(c.binaryToDecimal(c.XOR(abs(num1),abs(num2))))
            
        elif choice == '7':
            print("(",num1,")", num2, "=\n") 
            if num2<=10:     
                c.display(c.decimalToBase(abs(num1),abs(num2)))
            else:
                print(c.decimalToBase(abs(num1),abs(num2)))      
        
        # check if user wants to continue or quit
        next_calculation = input("Want another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input, Please enter a number between(1-7)")
        