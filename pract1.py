# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:09:31 2017

@author: User
"""
#1.Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a 
#single line.

a=[]
def que1():
   for num in range(2000,3200):
        if num%7==0 and num%5!=0:
            a.append(num)
   return a
            
            
print que1()    






2.

def fact(x):
    """factorial program"""
    if x==0:
        return 1
    else:
        return x * fact(x-1)
    
print fact(5)
     
3.

dict={}
def que3(x):
    for i in range(x):
        dict[i]=i**2
        
print dict

4.

x = raw_input("enter the values: ")
y = x.split(',')
print y
t = tuple(y)
print t


5.
x = raw_input("enter the string: ")
y = x.split(',')
print ','.join(sorted(y))



6.
#Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them 
# alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again

para = raw_input("enter the string: ")

newPara = ' '.join(list(set(para.split(' '))))

7.

#Write a program which accepts a sequence of comma separated 4 digit binary 
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated 
# sequence.
num =raw_input("enter the value:" )
temp =num.split(",")
for i in temp:
    x=int(i)
print x
if x%5==0:
    print "number is divisible by 5"
else:
    print "number is not divisible by 5"

8.

#Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a
# single line.

for x in range(1000,1050):
    if x%2==0:
        print (x),



##9.Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
##Suppose the following input is supplied to the program:


x = raw_input("enter the string: ")
d ={'upper_case':0,'lower_case':0}
for s in x:
    if s.isupper():
        d['upper_case']+=1
    else:
        d['lower_case']+=1
10.
#Use a list comprehension to square each odd number in a list. 
#The list is input by a sequence of comma-separated numbers.
#Suppose the following input is supplied to the program:

l1=raw_input("enter the element: ")
a=[int(x)**2 for x in (l1.split(',')) if int(x)%2!=0]

print a









