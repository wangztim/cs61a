def list_change(total, denoms):
    if total <= 0:
        return []
    if len(denoms) == 0:
        return []
    else:
        denom = denoms[0]
        if total < denom:
            return list_change(total, denoms[1:])
        else:
            change = []
            if (total == denom):
                change.append([total])
            for i in list_change(total - denom, denoms):
                dog = [denom]
                dog += i
                change.append(dog)
            change += list_change(total, denoms[1:])
            return change


print(list_change(10, [10, 5, 1]))
