import pytest
from operations import add , subtract , multiply ,divide

def test_add():
    assert add(1,3) == 4
    assert add(-1,2) == 1
    assert add(4,-5) == -1

def test_subtract():
    assert subtract(1,1) ==0 
    assert subtract(1,-1) ==2 
    assert subtract(-1 ,1) == -2

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(1,-2) == -2 
    assert multiply(-1,2) == -2 
    assert multiply(-1,-2) == 2
    assert multiply(-1,0) == 0
    
def test_divide():
    assert divide(-2,-1) == 2.0
    assert divide(0,2) == 0.0
    assert divide(14,-2) == -7.0 
    with pytest.raises(ZeroDivisionError , match="cant divide by zero !!!"):
        divide(2,0)
        divide(12312,0)
        
        
def test_power():
    assert power(1,100) == 1
    assert power(100,0) == 1
    assert power(2,2) == 4 
    assert power(4 , 0.5) == 2

    
def test_modulus():
    assert modulus(8 , 3) == 2
    assert modulus(9 , 3) == 0
    assert modulus(10, 3) == 1

def test_modulus_byzero():
    with pytest.raises(ZeroDivisionError , match="cant divide by zero !!!"):
        modulus(10,0)
    
    