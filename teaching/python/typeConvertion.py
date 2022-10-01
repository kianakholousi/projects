x = 8
y = 2.43
string1='5'
sum=x+y                          #Implicit Conversion   
# z = x+ string1                 #type error
int_sum = x + int(string1)       #Explicit Conversion
string_sum = str(x) + string1    #Explicit Conversion
print("x variable type",type(x))
print("y variable type",type(y))
print("sum variable type",type(sum))
print(sum)
print("s variable type",type(string1))
print("int_sum variable type",type(int_sum))
print(int_sum)
print("string_sum variable type",type(string_sum))
print(string_sum)
print(1+2) #concat