from HW8 import multy as mul
def test(a,b):
    test_c=mul(a,b)
    c=a*b
    assert c==test_c

test(10,10)
test(1,2)