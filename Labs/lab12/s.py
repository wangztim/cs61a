my_20_features = ["power", "marri", "captain", "nice", "weve", "huh", "play", "home", "tonight",
                  "ship", "men", "hous", "miss", "system", "wife", "dr", "boy", "fine", "cop", "hello"]

my_old_20_features = ["power", "captain", "weve", "world", "run", "three", "system", "ship",
                      "command", "move", "marri", "huh", "nice", "home", "hous", "miss", "boy", "wouldnt", "fine", "mother"]


def Diff(li1, li2):
    return (list(set(li1) - set(li2)))


print(Diff(my_old_20_features, my_20_features))
