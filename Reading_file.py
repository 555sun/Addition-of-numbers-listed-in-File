#print (" Enter the file name you want to process")
import re
fname = input("Enter file name you want to process\n")
fhand= open(fname)
x=0
for line in fhand:
    #print (line)
	line=line.rstrip()
	stuff=re.findall('[0-9]+',line)
	for i in stuff:
	   x=x+int(i)
	if len(stuff) != 1  : continue
	
	
	
print ("The sum of numbers in file is ",x)