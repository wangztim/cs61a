def reverse_number(n):
    """
    Returns the reverse of non-negative integer n
    >>> reverse_number(5)
    5
    >>> reverse_number(420)
    24
    >>> reverse_number(567)
    765
    >>> reverse_number(6666)
    6666
    """
    def recurse_helper(reg, rev):
        if reg < 10:
            if reg == 0:
                return rev
            else:
                return rev * 10 + reg
        next_last = reg % 10
        return recurse_helper(reg // 10, rev * 10 + next_last)
    return recurse_helper(n // 10, n % 10)


def get_first_digit(n):
    n_reversed = reverse_number(n)
    return n_reversed % 10


def get_all_but_first(orig):
    def count_num_digits(n, num_times_down):
        if n < 10:
            return num_times_down
        else:
            return count_num_digits(n // 10, num_times_down + 1)
    num_times_down = count_num_digits(orig, 0)
    return orig % pow(10, num_times_down)


def check_if_palindrome(n):
    """
    Returns True if n is the same as n-backwards, else false
    >>> check_if_palindrome(5)
    True
    >>> check_if_palindrome(420)
    False
    >>> check_if_palindrome(567)
    False
    >>> check_if_palindrome(6666)
    True
    >>> check_if_palindrome(424)
    True
    """
    n_reversed = reverse_number(n)

    return n == n_reversed


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
