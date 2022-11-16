#!/usr/bin/python3
#

#-------------------------------checkPrime
#
#素数チェック関数
#戻り数
#    True  : 素数
#    False : 素数ではない
#
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


#素数ｎは、２以上(n-1)以下の整数で割り切れなければ、素数と判定できる。
#If the prime number n is not divisible by an integer of 2 or more (n-1) or less, it can be determined to be a prime number.