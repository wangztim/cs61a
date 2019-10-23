class Ok:
    py = [3.14]

    def __init__(self, py):
        self.ok = self.py
        Ok.py.append(3 * py)

    def my(self, eye):
        print(self.my(eye))
        return self.ok.pop()

    def __str__(self):
        return str(self.ok)[:4]


class Go(Ok):
    def my(self, help):
        return [help + 3, len(Ok.py)]


oh = Go(5)
Go.py = [3, 1, 4]
oh.no = {"just": Go(9)}
