# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cmath
import math

def calculateResultsOfEquation(a,b,c,d):
    if( a == 0):
        print("Wartość 'a' musi być różna od zera")
        return
    q = ((3 * a * c) - (b ** 2)) / ((a ** 2) * 9)
    r = ((9 * a * b * c) - (27 * (a ** 2) * d) - (2 * (b ** 3))) / ((a ** 3) * 54)
    qPlusR = (q ** 3) + (r ** 2)
    delta = (b ** 2 * c ** 2) - (4 * a * c ** 3) - (4 * b ** 3 * d) - (27 * a ** 2 * d ** 2) + (18 * a * b * c * d)
    if(delta > 0):
        s = (r + cmath.sqrt(qPlusR)) ** float(1 / 3)
        t = (r - cmath.sqrt(qPlusR)) ** float(1 / 3)
    elif(delta < 0):
        s = abs(r + cmath.sqrt(qPlusR).real) ** float(1 / 3)
        t = abs(r - cmath.sqrt(qPlusR).real) ** float(1 / 3)
        if(r + cmath.sqrt(qPlusR).real < 0):
            s = s * -1
        if(r - cmath.sqrt(qPlusR).real < 0):
            t = t * -1
    if(delta == 0):
        if(b ** 2 == 3 * a * c):
            x1 = -1 * b / 3 * a
            x2 = x1
            x3 = x2
        else:
            x1 = ((9 * a * d) - (b * c)) / ((2 * b ** 2) - (6 * a * c))
            x2 = x1
            x3 = ((4 * a * b * c) - (9 * (a ** 2) * d) - b ** 3) / ((a * b ** 2) - (3 * (a ** 2) * c))
        print("x1: " + str(x1))
        print("x2: " + str(x2))
        print("x3: " + str(x3))
        return
    x1 = complex(s + t - (b / (3*a)),0)
    x2 = complex(-1 * ((s + t)/2) - b / (3 * a), (s - t)*(cmath.sqrt(3)/2))
    x3 = complex(-1 * ((s + t)/2) - b / (3 * a), -1 * (s - t)*(cmath.sqrt(3)/2))
    if(x1.imag):
        print("x1: " + str(round(x1.real, 3) + round(x1.imag, 3) * 1j))
    else:
        print("x1: " + str(round(x1.real, 3)))
    if (x2.imag):
        print("x2: " + str(round(x2.real, 3) + round(x2.imag, 3) * 1j))
    else:
        print("x2: " + str(round(x2.real, 3)))
    if (x3.imag):
        print("x3: " + str(round(x3.real, 3) + round(x3.imag, 3) * 1j))
    else:
        print("x3: " + str(round(x3.real, 3)))
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.

print("Podaj wartosc a: ")
a = float(input())
print("Podaj wartosc b: ")
b = float(input())
print("Podaj wartosc c: ")
c = float(input())
print("Podaj wartosc d: ")
d = float(input())
calculateResultsOfEquation(a,b,c,d)

