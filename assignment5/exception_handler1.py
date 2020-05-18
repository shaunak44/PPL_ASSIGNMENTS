#this programme handles all exception using same handler code

def h():
    input()

def g():
    i = int(input())
    j = int(input())
    k = i / j
    print (k)
    print ("Hi There")
    h()

def f():
    g()
    print ("G is over")

for i in range(0,4):
    try:
        f()
    except:
        print ("Exception occured, but continuing")