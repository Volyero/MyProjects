#!/usr/bin/python3
#
pcode = '*'
for i in range(10):
    print(pcode * i)
    
#--------------
    
pcode = '123-4567'
print(pcode)
print(pcode[0:8])
print(pcode[0:7] + pcode[0:1])
print(pcode[:3] + pcode[4:])



#---------------
def postal(pcode):
    return pcode[:3] + pcode[4:]
#--------------------
print(postal('123-4567'))
print(postal('999-8888'))
#----------------------

def postal2(pcode):
    return pcode[:3] + '-' + pcode[3:]
print(pcode):