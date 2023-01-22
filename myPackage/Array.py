'''
Created on Jan. 15, 2023

@author: sarat
'''
from array import array

str="this is a td bank interview td"

strList = str.split()

print(strList)

homecount=0

for i in strList:
 if i=="td":
        homecount = homecount+1
        
print(homecount)

