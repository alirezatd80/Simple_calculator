def add(num1:int , num2 :int ):
    return num1+num2


def subtract(num1:int , num2:int):
    return num1-num2 

def multiply(num1:int , num2:int):
    return num1*num2

def divide(num1 :float , num2:float) :
    if num2 == 0 :
        raise ZeroDivisionError('cant divide by zero !!!')
    return num1/num2

def power(num1 :int , num2 :int):
    return num1 ** num2

def modulus(num1 :int , num2 :int):
    if num2 == 0:
        raise ZeroDivisionError('cant divide by zero !!!')
    return num1 %num2
def root(num1 :int , num2=0.5):
    return num1 ** num2