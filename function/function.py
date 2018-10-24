
def fib(n):
    print "Fonction fibonnaci"
    a, b = 0, 1

    while a < n :
        print a
        a, b = b, a + b

fib(2000)
