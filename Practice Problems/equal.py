from tree import *


def equal(t1, t2):
    """Returns Tree if t1 and t2 are equal trees.

    >>> t1 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> t2 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> equal(t1, t2)
    True
    >>> t3 = Tree(1,
    ...           [Tree(2),
    ...            Tree(3, [Tree(4)])])
    >>> equal(t1, t3)
    False
    """
    "*** YOUR CODE HERE ***"
    if t1 and t2:
        if t1.is_leaf() and t2.is_leaf():
            return t1.label == t2.label
        if len(t1.branches) == len(t2.branches):
            results = []
            for i in range(len(t1.branches)):
                results.append(equal(t1.branches[i], t2.branches[i]))
            return all(results)
        return False
    if (t1 == None and t2) or (t2 == None and t1):
        return False
    else:
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
