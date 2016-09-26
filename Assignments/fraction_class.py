"""
Name: Jeron Amory
Email: j.amory268@gmail.com
Assignment: Homework 2 - Fraction Class
Due: 26 Sep @ 1:00 p.m.
"""

import sys

def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n

class fraction(object):
    def __init__(self,n,d):
        self.numerator = int(n / gcd(abs(n), abs(d)))
        self.denominator = int(d / gcd(abs(n), abs(d)))

    def __str__(self):
        return "%s/%s" % (self.numerator, self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return str(fraction(self.numerator,self.denominator)) + ' ' + 'x' + ' ' + str(fraction(rhs.numerator,rhs.denominator)) + ' ' + '=' + ' ' + str(fraction(x,y))
        
    def __add__(self, other):
        addNum = self.numerator*other.denominator + self.denominator*other.numerator
        addDenom = self.denominator*other.denominator
        if addNum > addDenom:
        	whole = int(addNum / addDenom)
        	return str(fraction(self.numerator, self.denominator)) + ' ' + '+' + ' ' + str(fraction(other.numerator, other.denominator)) + ' ' + '=' ' ' + str(whole) + ' ' + str(fraction(addNum % addDenom, addDenom))
        else:
        	return  str(fraction(self.numerator, self.denominator)) + ' ' + '+' + ' ' + str(fraction(other.numerator, other.denominator)) + ' ' + '=' ' ' + str(fraction(addNum % addDenom, addDenom))
        	
        	
def main():
	a = fraction(3,5)
	b = fraction(1,5)
	c = a * b
	d = a + b
	print(c)
	
main()
        

if __name__ == '__main__':
	main()
