
def repeat(k):
    """When called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5

1
 """
    return detector(lambda n: False)(k)


def detector(f):

    def g(i):
        print(f)
        if f(i):
            print(i)
        return detector(lambda n: n == i or f(n))
    return g


repeat(7)(1)(7)

## detector
    #f: func that returns false
    #i: 7

## detector2
    #f func that returns false, func that checks if n == 7

## detector3
    #f func that checks if false or n == 7 or n == 1
