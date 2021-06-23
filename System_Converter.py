################### Function Blocks ##############################
def binary_to_decimal(num):
    num=str(num)
    binary=n=0
    bin1=num[::-1]
    for i in bin1:
        binary=binary+(int(i)*(2**n))
        n+=1
    return str(binary)

def decimal_to_binary(num):
    st=""
    n=num
    a=0
    x=int(num)
    while x>0:
        a=int(n)
        st=str(a%2)+st
        n=str(a//2)
        x=a//2
    return st

def octal_to_decimal(num):
    p=octa=0
    rev=num[::-1]
    for i in rev:
        n=int(i)*(8**p)
        octa=octa+n
        p+=1
    return octa

def decimal_to_octal(num):
    n=int(num)
    s=""
    while n!=0:
        s=s+str(n%8)
        n=n//8
    octa=str(s)[::-1]
    return octa

def decimal_to_hexa(num):
    n=int(num)
    s=""
    i=0
    ch=""
    while n!=0:
        i=n%16
        if i>9:
            s=s+chr(i+55)
        else:
            s=s+str(i)
        n=n//16
    return s[::-1]

def hexa_to_decimal(num):
    num=num.upper()[::-1]
    n=0
    p=0
    hex=0
    for i in num:
        if ord(i)>=65: 
            n=(ord(i)-55)*(16**p)
        else: 
            n=int(i)*(16**p)
        hex=hex+n
        p+=1
    return str(hex)
        
def binary_to_octal(num):
    dec=binary_to_decimal(num)
    oct=decimal_to_octal(dec)
    return oct

def binary_to_hexa(num):
    dec=binary_to_decimal(num)
    hex=decimal_to_hexa(dec)
    return hex

def octal_to_binary(num):
    dec=octal_to_decimal(num)
    binary=decimal_to_binary(dec)
    return binary

def octal_to_hexa(num):
    dec=octal_to_decimal(num)
    hexa=decimal_to_hexa(dec)
    return hexa

def hexa_to_binary(num):
    dec=hexa_to_decimal(num)
    binary=decimal_to_binary(dec)
    return binary

def hexa_to_octal(num):
    dec=hexa_to_decimal(num)
    octa=decimal_to_octal(dec)
    return octa