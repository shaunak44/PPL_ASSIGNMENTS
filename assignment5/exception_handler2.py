#!/usr/bin/python
"""This program handles all 3 exceptions separately."""
def zerohandler():
    print("Divide by Zero Exception occured")  
def ctrldhandler():
    print("Keyboard interrupt exception occured")
def badinthandler():
    print("Enter numeric value") 
def f():
    k = 0
    i = int(input())
    j = int(input())
    k = i / j
    print(k)
for counter in 1,2,3,4:
    try:
        f()
    except ZeroDivisionError:
        zerohandler()
    except EOFError:
        ctrldhandler()
    except ValueError:
        badinthandler()
    finally:
        print ("Finally executed")