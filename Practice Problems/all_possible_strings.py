def all_possible_strings(input_set, length_limit, base=""):
    accumulator = 0
    for element in input_set:
        val = base + element
        if (len(val) == length_limit):
            accumulator += 1
        else:
            accumulator += all_possible_strings(input_set, length_limit, val)
    return accumulator


print(all_possible_strings({"a": "a", "b": "b", "c": "c"}, 3))
