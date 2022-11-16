#!/usr/bin/python3
#
print("Search-1")
for num in range(2, 101):
    flg = True
    for i in range(2, num):
        if num % i == 0:
            flg = False
            break;
    if flg:
        print (' ' + str(num), end='')
print()

print("Search-2")

def checkPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
#-------------------------------main
#num : 素数候補(prime number choice)

for num in range(2, 101):
    if checkPrime(num):
        print(' ' + str(num), end='')
print()