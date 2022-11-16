#!usr/bin/python3
#アベドアリ
#2021/12/02
def pyramid(n):
    for i in range(n):
        p  = ' ' * (n - i - 1)
        p += '@' * (i * 2 + 1)
        print(p)
#------------------------main
pyramid(5)

def bmi(h, w):
    hantei = '標準'
    bmi = w / (h * h)
    if bmi < 18.5:
        hantei = '痩せすぎ'
    elif bmi >= 30:
        hantei = '高度肥満'
    elif bmi >= 25:
        hantei='肥満'
    
    print('BMI    =', bmi)
    print('判定  =', hantei)
#------------------------main
bmi(1.7, 80)