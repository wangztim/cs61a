def gen_list(n):

    return [list(range(i + 1)) for i in range(n)]


def gen_inc_list(n):

    return [list(range(sum(range(i + 1)), sum(range(i + 2)))) for i in range(n)]
