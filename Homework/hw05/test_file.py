from hw05 import *

t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
t = Tree(1, [Tree(2), Tree(3)])


def gen_paths(t):
    if t.is_leaf():
        return [t.label]

    paths = []

    for b in t.branches:
        path = [t.label]
        route = gen_paths(b)
        path.extend(route)
        paths.append(path)

    return paths


print(gen_paths(t1))
