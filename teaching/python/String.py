# #assigning String to a variable
name = "john" #same as name = 'john'
print("Hello" + name)
lastName = "smith"
info = name + " " + lastName
print(info)

# #indexing
print(name[2]) #index starts from 0
# print(name[len(name)]) #index error
print(name[len(name)-1]) #last index
print(name[-1]) #also last index

# #multiple line String
a ='''python is a programming language.
Python can be used to handle big data.
Python syntax is easy to learn.''' #used for printing without deformation
# print(a)
print("python is a programming language.\nPython can be used to handle big data.\nPython syntax is easy to learn")
# #lenght of String can be accessed by len(StringName) 
print(len(a))

# #checking for substrings
print("python" in a)

#iteration
for x in "banana":
   print(x)

# insert numbers into strings with format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#can have unlimited number of arguments
quantity = 3
itemNo = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemNo, price))
#to make sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# #slicing
c = "Hello, World!"
print(len(c))
print(c[-1:3]) #empty string
print(c[3:-1])
print(c[1])
print(c[2:5])   # index 2 to index 5 (not included)
#slicing from the start
print(c[:5])
#till the end
print(c[2:])    # index 2, and all the way to the end
#Negative Indexing(to start the slice from the end of the string)
print(c[-5:-2]) # index -5 to index -2 (not included)
print(c[-1]) # negetive index starts to count backward from the end

# #operation on String
s= "Hi"
print(s*3)
print("1"+"2")

#string methods
greeting = "Hello World!"
newList = ["Python","is","fun","to","learn"]
myString=","
newString = "python is a programming languge" 
print(greeting.upper())
print(greeting.lower())
print(greeting.capitalize())
x= greeting.replace("World","friend")
print(x)
print(greeting)
print(myString.join(newList))
print(newString.split(" "))
print(greeting.rfind("ll"))
print(greeting.count("l"))
print(greeting.find("l")) #returns first index 
print(greeting.find("l",4)) #starts searching from index 5
print("   statement   ".strip()) #remove white space from start and end


# immutable
sentence ="qython is a programming language"
# sentence[0]="p" #error cant access string items
sentence="python is fun to learn" #but you can assign a whole new value to the same variable
# print(sentence)
new_sentence = "p" + sentence[1:]
# print("new sentance: "+new_sentence)
sentence = "p" + sentence[1:]
# print("sentance: "+sentence)

# get a sub string with find method
str = 'X-DSPAM-Confidence:0.8475'
start_index = str.find("-")
# end_index = len(str)
# end_index = str.find('5')+1
end_index = str.rfind('-')
subString = str[start_index+1:end_index]
print(subString)
