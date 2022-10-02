# #creating a list
li = [2,"banana",3.4,False]
# print(li)
# print(type(li))
Li1 = list() #empty list
# print(Li1)
Li2 = list([3,5,6])
# print(Li2)
L1 = list(i*2 for i in li)
L2 = [x for x in range(101) if x % 2 == 0]
# # print("L1=",L1)
# # print("l2=",L2)

# # List constructor
Li3 = list(("apple","banana","cherry"))
# # print(Li3)

# #indexing
print("forth item of list =",li[0])
print(li[-1]) #start count from the end
print(len(li))
print(li[len(li)-1])


#iteration
# li = [2,"banana",3.4,False]
print(li*2)

for a in li:
    print(a*2,end=" ")
    
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
    
# #in keyword    
print(2 in li)
print("ba" in li)
print("ba" in "banana")

# # operation
print([1,2]+[3,4])
print([1,2]*2)
print(li*2)    
print(li+["hello",5])

# # slicing
x=[2,5,3,1,6,8,9]
print(x[1:4])
print(x[:2]) 
print(x[3:]) 
print(x[::2]) 
print(x[1:6:3]) 
print(x[5:3:-1])
list = [1,2,3,4,5] 
print(list[-1::]) # list only with last element
print(list[:-1:]) # all list except last element
print(list[::-1]) # list in backwards order
print(list[-4:-1:-1])

# changing item\s list
L=[27,51,80,34,93]
L[3]=17
print(L)
L[1:3]=[22,37]
print(L)
L[2:4]=[99] 
# print(L)

# copy a list
list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
list1[2]="orange"
list3 = list1[:]
# print(list2)
# print(list3)

newlist = [2.7,23,3.4,94]
#list function
print("list lenght =",len(newlist))
print(max(newlist))
print(min(newlist))
del newlist[2] #removes specified index
# print(newlist)
del newlist
# print(newlist)

# # list methods
mylist = [2,3,5,2]
thislist= [5,37,29]
# adding to a list
mylist.append(1)
# print(mylist)
mylist.insert(1,10)
# print(mylist)
mylist.extend(thislist)
# print(mylist)

mylist.sort() # alphanumerically, ascending
# print(mylist)
mylist.sort(reverse = True) #alphanumerically, descending
# print(mylist)
mylist.reverse()
# print(mylist)

print(mylist.count(2))
print(mylist.index(5))

# print(mylist)
mylist.remove(2) #remove first index of a value
# print(mylist)
mylist.pop(1) #delete specified index item
# print(mylist)
mylist.pop() #delete the last value
# print(mylist)
thislist.clear() #delete the whole list
# print(thislist) #error name not defined

# # comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
# print(newlist)
newlist = [x for x in fruits if x != "apple"]
# print(newlist)
newlist = ["i love "+x for x in fruits]
# print(newlist)
newlist = [x for x in range(10)]
# print(newlist)
newlist = [x*2 for x in range(10) if x < 5]
# print(newlist)
newlist = [x.upper() for x in fruits]
# print(newlist)
newlist = ['hello' for x in fruits]
# print(newlist)
newlist = [x if "banana" else "apple" for x in fruits]
print(newlist)

#Multi-Dimensional Lists
my2DList = [[1, 2,3], 
            [4, 5, 6]]
print(my2DList)
print(len(my2DList)) #number of rows
print(len(my2DList[1])) #number of columns
print(my2DList[0][0]) #first elemnt access items 2DlistName[index][index]

for i in my2DList:
    print(i)
    
for i in range(len(my2DList)) : 
    for j in range(len(my2DList[i])) : 
        print(my2DList[i][j], end=" ")
    print()  

multlist = [[0 for columns in range(4)] for rows in range(3)]
# print(multlist)
for column in multlist:
    for item in column:
        print(item, end = " ")
    print()
    
lst = [
  ['John',18],
  ['Jim',29],
  ['Jason',23] ]

lst.sort(key=lambda x:x[0],reverse=False) #key = sort by column
print(lst)

