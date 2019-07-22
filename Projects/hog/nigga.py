def printed(fn):
    def print_and_return(*args):
        result = fn(*args)
        print('Result:', result)
        return result
    return print_and_return


printed_pow = printed(print)
printed_pow(2, 8, 69)
