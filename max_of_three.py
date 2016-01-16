#-*-coding: utf-8 -*-
"""
Define a function max() that takes three numbers as arguments and returns the
largest of them. Use the if-then-else construct available in Python. (It is
true that Python has the max() function built in, but writing it yourself is
nevertheless a good exercise.)
"""

def _max(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

if __name__ == "__main__":
    #z is largest
    test_1 = _max(1,2,3)
    print('Z should be largest:', test_1)

    #y is largest
    test_2 = _max(1,3,2)
    print('Y should be largest:', test_2)

    #x is the largest
    test_3 = _max(3,1,2)
    print('X should be largest:', test_3)


