from src.maths_ops import  add,substract,multiply,divide


def test_add():
    assert add(2,3)==5
    
def test_sub():
    assert substract(3,2)==1

def test_multiply():
    assert multiply(4,3)==12

def test_divide():
    assert divide(10,2)==5
    