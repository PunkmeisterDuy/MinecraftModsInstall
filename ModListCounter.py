import os

file = open("ModList.txt", "r")
count = 0

for i in file:
    if (i.find("#") < 0):
        count +=1
        
print(count)
