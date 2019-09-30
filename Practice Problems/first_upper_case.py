def string_trimmer(string):
    if len(string) > 1:
        return string[1:]
    else:
        return ""


def first_upper_case(string):
    if len(string) == 0:
        return ""
    if string[0].isupper():
        return string[0]

    else:
        return first_upper_case(string_trimmer(string))


print(first_upper_case("NigggeKsdfls"))
