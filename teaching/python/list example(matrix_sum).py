import random
def buildSquareMatrix(m, n):    
	if m == n:        
		matrix = []        
		for i in range(m):            
			r = []            
			for j in range(n):
				r.append(random.randint(1, 100))
			matrix.append(r)
		return matrix        
	else:        
		return "This function builds only square matrices with random integers\n"
def addMatrices(a, b):    
	m = n = len(a)    
	c = []    
	for i in range(m):        
		r = []        
		for j in range(n):            
			r.append(a[i][j] + b[i][j])        
		c.append(r)                
	return c
def printMatrix(a):    
	for i in a:        
		for j in i:            
			print(j, end = "\t")        
		print()    
	print()

a = buildSquareMatrix(5, 5)
b = buildSquareMatrix(5, 5)
printMatrix(a)
printMatrix(b)
c = addMatrices(a, b)
printMatrix(c)