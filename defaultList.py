class DefaultList(list):
    def __init__(self, default_value):
        super().__init__()
        self.default_value = default_value

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value


s = DefaultList(5)
s.extend([4, 10])

indexes = [1, 124, 1882]
for i in indexes:
    print(s[i], end=" ")