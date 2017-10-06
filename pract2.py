# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 17:02:46 2017

@author: User
"""

9.
# sorting dictionary by values
a={1:'pritam',2:'shakti',3:'abc',4:'xyz'}
for x in sorted(a.values()):
    print x,

    
# sorting dictionary by key
for x in sorted(a.keys()):
    print x
    
# sorting dict by length
s=['asas','sd','s']
print sorted(a,key=len)


x=(12,23,12,345,123,1,34,45)
x=sorted(x)
print x


x=(1,2,3,4,2,32,1)
x=sorted(x)

10.

#Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown 
# as following:
#D 100
#W 200

balance = 0
while 1:
#    balance = 1
    ch = input("enter the input(1 for deposite 2 for withdrawl:")
    if ch==1:
        amount= input("enter amount: ")
        balance = balance +amount
        print balance
    else:
        amount = input("enter the amount")
        balance = balance-amount



# search pattern
import re

a=['sasas','sdsd','werr','tght','yhyh','pritam']

re.search('pritam',str(a))


a=re.search('pritam',str(a))

a


print a.group()



































