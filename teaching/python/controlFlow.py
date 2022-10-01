# #while
i=1
while i<10:
    print(i)
    i+=1
    
# #for
x="banana"
print(x*2)
for s in "banana":
    print(s*2, end="")

sum= 0
for x in range(10):
    sum += x
    print(x,sum)
print(sum)        

li = [1,6,4,76,23]
print(li*2)
for l in li:
    print(l*2,end=" ")

# #break & continue
i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  if i ==8:
      break
  print(i)

for i in range(100):
    if(i==3):
        continue
    if(i==10):
        break
    print(i)


# loop else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# for else wont execute if exit loop using break
for x in range(6):
  print(x)
else:
  print("Finally finished!")