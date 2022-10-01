# star patterns
# Program to print right Half Pyramid
num_rows = int(input("Enter the number of rows: "));
k = 0
for i in range(0, num_rows):
    for j in range(0,i): #set to range(num_ros,k,-1) and check out the result
        print("*", end=" ")
    k = k + 1
    print()
    
# # Program to print full pyramid 
num_rows = int(input("Enter the number of rows: "));
for i in range(0, num_rows):
	for j in range(0, num_rows-i-1):
		print(end=" ")
	for j in  range(0, i+1):
		print("*", end=" ")
	print()
 
# # Program to print One More Star Pattern Pyramid
num_rows = input("Enter maximum stars you want display on a single line: ")
num_rows = int (num_rows)
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")
# #dimond
num_rows = int(input("Enter the number of rows: "))
k = 0
for i in range(0, num_rows): 
    for j in range (1, (num_rows - i) + 1): 
        print(end = " ")          
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0   
    print()  
 
k = 2
m = 1
for i in range(1, num_rows): 
    for j in range (1, k):
        print(end = " ") 
    k = k + 1	  
    while m <= (2 * (num_rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1	
    print() 
    