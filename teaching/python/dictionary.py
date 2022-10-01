dict1 = {"NUM":[45,23,24], 1000:"coding", 2000:4.5, 3.4:7, "XXX":89} 
# print(dict1)     
ages = {"dave":34, "sarah":23, "john":56}
print(ages["sarah"])

Name =["dave","sarah","john"]
age = [34,23,56]
x=Name.index("sarah")
print(age[x])

# bad_dict = { [1, 2, 3]:"one two three"  } #cant use immutable objects for keys
good_dict = { "one two three":[1, 2, 3]  }
# print(bad_dict)

print(type(ages))
print(len(ages))
print(ages)

# indexing
print(ages["dave"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# print(thisdict)

dict = {"brand": "Ford",
             "model": "Mustang",
             "year": 1964,
             "year": 2020}
# print(dict)

# #iteration
for i in thisdict: #returns key names
    print(i)

for x in thisdict: #returns values
  print(thisdict[x])    
  
for x in thisdict.values():
  print(x) 

for x in thisdict.keys():
  print(x)
  
for x,y in thisdict.items(): #returns both key and value
  print(x.upper(),y*2)
     
# dict method
# acssessing item
print(ages["mike"])
print(ages.get("mike")) #.get(key)=value

x= ages.values() #list view of values
print(x)
ages.update({"mike":19})
print(x)
ages["sarah"]=25
print(x)
#same for
x= ages.keys() #list view of keys
x=ages.items()
print(ages.items()) #list view of key and value pairs
print(x)
ages.update({"mike":19})
print(x)
ages["dave"]=43
print(x)

print(ages)
ages.update({"mike":25})
ages["sarah"]=30
print(ages)
ages["brad"]=60
print(ages)

#check for existing key
if "dave" in ages:
    print("yes") 
else:
  print("no")    
print("john" in ages) 
print(ages.setdefault("john",-1))
print(ages.setdefault("amy","this key is not in the dictionary"))

# deleting items 
ages = {"dave":34, "sarah":23, "john":56,"mike":25} 
print(ages)    
ages.pop("sarah")   
print(ages) 
ages.popitem()
print(ages) 
del ages["dave"]
print(ages) 
ages.clear()
print(ages) 
del ages
print(ages)
    
# operation
ages1 = {"dave":34, "sarah":23, "john":56} 
ages2 = {"mike":18, "amy":32, "phill":40} 
print(ages1+ages2)
print(ages*2)

# mutable
def func(dict):
  dict.update({3:20}) #change or add value
  print("inside func",dict)
  
dict = {1:2,4:6,10:5}
print("before func",dict)    
func(dict)
print("after func",dict)  

# Dictionary Comprehension
squares = {str(x)+" second order": x*x for x in range(6)}
print(squares)
odd_squares = {x: x**2 for x in range(11) if x % 2 == 1}
print(odd_squares)

# Built-in Functions to use on Dictionary 
squares = {10: 100, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(all(squares))
print(any(squares))
print(len(squares))
print(sorted(squares))

# nested dictinary
myfamily = {
  "child1" : {
    "name" : "Emily",
    "year" : 2004
  },
  "child2" : {
    "name" : "Toby",
    "year" : 2007
  },
  "child3" : {
    "name" : "Mike",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
