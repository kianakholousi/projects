# class definition for calculator 
from binconversion import Binary_conversion
class Calculator(Binary_conversion): 
    
    def __init__(self) -> None:
        # super().__init__() 
        self.flag=0 #for not repeating binary convertion (readyforcomputation())

    def readyforcomputation(self,a,b):
        # decimal to binary
        a=super().decimalToBinary(a)
        b=super().decimalToBinary(b)
        # Equalize the length of two binary numbers by adding zeros to the left/before the first digit
        d=len(a)-len(b)
        if d>0:
            b=abs(d)*"0" +b
        elif d<0:
            a=abs(d)*"0"+a
        return a,b
        
    # performs addition like a full Adder 
    def add(self,a,b,c="0"): 
        res=""
        Sum=""
        if self.flag==1:
            a,b=self.readyforcomputation(a,b)
        for i in reversed(range(len(max(a,b)))): #same as range(len(max(a,b))-1,-1,-1)
            Sum=self.XOR(c,self.XOR(a[i],b[i]))  #Sum= a^b^c (a Xor b Xor c) for each bit
            c = (self.OR(self.OR(self.AND(a[i],b[i]),self.AND(a[i],c)),self.AND(b[i],c))) #c = a.b + b.c +a.c for each bit, c_in(0)=0 c_in(i)=c_out(i-1)
            # c = self.OR(self.AND(self.XOR(a[i],b[i]),c),self.AND(a[i],b[i]))
            res = Sum + res
        if self.flag!=2:    
            res = c + res
        return res               

    # performs addition like a full Adder-Subtractor
    def subtract(self,a,b): 
        A,B=a,b
        if self.flag==2:
            a,b=self.readyforcomputation(a,b)
        one = "1"*len(b)
        b=self.XOR(b,one)  #b XOR 1 = b' (one's complement) 
                            #same as
                            # for i in range(len(max(a,b))):
                                # B.append(self.XOR(b[i],"1"))   
                            # b="".join(B)
        diff=self.add(a,b,"1") #a-b=a+b'+1 ((b'+1)two's complement)
        if (A>B):
            return diff
        else:                                         #when diff<0 retun two's complement of diff
            one = "1"*len(diff)
            diff= self.add(self.XOR(diff,one),"1") #d=d'+1(two's complement)
            return diff

    # performs binary multiplication using full Adder, AND logic gate
    def multiply(self,a,b):
        if self.flag==3:
            a,b=self.readyforcomputation(a,b) 
        res = ""              
        for k, j in enumerate(range(len(b) - 1, -1, -1)): #k from 0 - len(b) j from len(b) to 0 (len(a)=len(b))
            tmp = ""
            # computing each row of the multiplication
            tmp = tmp + '0' * k  # shift k to the left
            for i in reversed(range(len(a))):
                tmp = self.AND(a[i],b[j]) + tmp 
            # equalizing the length of tmp,res (binary numbers) by adding zeros to the left/before the first digit
            d=abs(len(tmp)-len(res))
            if d>0:
                res=d*"0" +res
            elif d<0:
                tmp=d*"0"+tmp 
            #adding rows to each other   
            res = self.add(res, tmp)
        return res

    def AND(self,a,b):
        res=""
        if self.flag==0:
            a,b=self.readyforcomputation(a,b)
        for i in range(len(max(a,b))):  # a&b =1 if a=b=1 for each bit
            if (a[i]=="1" and b[i]=="1"): 
                res+="1"
            else:
                res+="0"                 
        return res 
    
    def OR(self,a,b):
        res=""
        if self.flag==0:
            a,b=self.readyforcomputation(a,b)  
        for i in range(len(max(a,b))): # a|b =0 if a=b=0 for each bit
            if (a[i]=="0" and b[i]=="0"):
                res+="0"
            else:
                res+="1"                       
        return res 
    
    def XOR(self,a,b):
        res=""
        if self.flag==0:
            a,b=self.readyforcomputation(a,b)
        for i in range(len(max(a,b))): # a^b =1 if (a=1,b=0 or a=0,b=1) a!=b for each bit
            if (a[i]!=b[i]):
                res+="1"
            else:
                res+="0"                        
        return res
    
    def decimalToBase(self,num,base):  
        """converting a decimal number to any Base is done by performing repeated division operations on num by base until 0 is reached, 
        taking remainders after each operation which are then appended to the result. The string is then reversed before being returned.
        If the remainder does not constitute one of the digits 0-9, an uppercase letter A-Z will be used to represent the remainder instead.  
        Args:
            num decimal(int): input decimal number
            base (int): convertion base
        Returns:
            res(string): n(decimal input) converted to base(b)
        """
        res= ""
        while num>0:
            digit = int(num%base)
            if digit<10:
                res += str(digit)
            else: #ord() gets char return uni code, gets char 
                res += chr(ord('A')+(digit-10))  #Using uppercase letters (to start from A digit(>10)-10)
            num //= base
        res = res[::-1]  #To reverse the string
        return res 
    
    #gets decimal(int) input and prints numbers in seven segment format  
    def display(self,number):
        # seven segment display
        ssd = {
        '0': ('***', '* *', '* *', '* *', '***'),
        '1': ('  *', '  *', '  *', '  *', '  *'),
        '2': ('***', '  *', '***', '*  ', '***'),
        '3': ('***', '  *', '***', '  *', '***'),
        '4': ('* *', '* *', '***', '  *', '  *'),
        '5': ('***', '*  ', '***', '  *', '***'),
        '6': ('***', '*  ', '***', '* *', '***'),
        '7': ('***', '  *', '  *', '  *', '  *'),
        '8': ('***', '* *', '***', '* *', '***'),
        '9': ('***', '* *', '***', '  *', '***'),
        '.': ('   ', '   ', '   ', '   ', '  *'),
        '-': ('   ', '   ', '  -', '   ', '   '),
        }
        digits = [ssd[digit] for digit in str(number)]
        for i in range(5):
            print("  ".join(part[i] for part in digits))
            