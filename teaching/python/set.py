set1 = {"egg", "bread", "pepper"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4= {"python", 3, True, 3.10}
mathConstants =set([3.1415,2.7182])
# print(set4)
# print(mathConstants)
# my_set = {1, 2, [3, 4]} #sets can't have mutable values

#Constructor
thisset = set(("hi", "hello", "hey")) # note the double round-brackets
# print(thisset)

#empty set
a = {}
# print(type(a))
a = set()
# print(a)
# print(type(a))

# print(set4)
# print(type(set1))
# print(len(set1))

# changing item
set1 = {"egg", "bread", "pepper"}
# set1[1]="new"

# indexing
# print(set1[1]) #error not set items dont have key or index

#iteration
set4= {"python",3,True,3.10}
for x in set4:
    print(x*2,end=" ")
    
# in key word
if 3 in set4:
    print("Yes")
else:
    print("No")  
print(thisset)  
print("hi" in thisset)    
print("bye" in thisset)    

# method
set1 = {"egg", "bread", "pepper"}
set2 = {1, 5, 7, 9, 3}
set1.add("milk")
# print(set1)
set2.update({11,13,15,17,19})
# print(set2)
newset={11,13,15,17,19}
set2.update(newset)
# print(set2)
set2.union(newset)
# print(set2)
list1=[21,23,25,27,29]
dict1={0:31,1:33,2:35,3:37,4:39}
tup1=(41,43,45,47,49)
set2.update(list1)
# print(set2)
set2.update(dict1)
# print(set2)
set2.update(tup1)
# print(set2)

set2.remove(0)
# print(set2)
# set2.remove(20) #error.
set2.discard(2)
# print(set2)
set2.discard(10)
# print(set2)
x=set2.pop() 
# print(set2,x)
# del set2[1] #error
set2.clear()
# print(set2)
del set2
# print(set2)

# funcs
Fset= {0,2,26,4,65,92,41,86}
print(all(Fset))
print(any(Fset))
print(list(enumerate(Fset)))
print(len(Fset))
print(max(Fset))
print(min(Fset))
print(sum(Fset))
print(sorted(Fset))

# pass by reference
def func1(seeet):
    seeet.add(5)
    # print("in",seeet)
  
seeet={1,2,3}    
# print("before",seeet) 
func1(seeet)
# print("after",seeet)     