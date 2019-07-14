# -*- coding: utf-8 -*-
#loops

#for loop

for i in range(1,5):
    print(i, end=' ')
    
for i in range(1, 20):
    if i%2==0:
        print(i, 'is even number')
        
for i in range(1, 100):
    if i%i==0 and i%2>0 and i%3>0 and i%5>0:
        print(i, 'is prime number')

#while

while True:
    s = input("Enter something, end to exit :  ")
    if s == 'end':
        break;
    if (len(s) < 3):
        print('small text')
        continue

        