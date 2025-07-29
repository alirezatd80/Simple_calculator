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