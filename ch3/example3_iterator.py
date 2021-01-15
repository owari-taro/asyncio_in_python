class A:
    def __iter__(self):
        # initial value
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x

#see python tric p170
class Repeater:
    def __init__(self, value):
        self.value = value
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 100:
            raise StopIteration
        self.count += 1
        return self.value


if __name__ == "__main__":
    a = A()
    for i in a:
        print(i)
    for i in a:
        print(i)

    test = Repeater("test")
    for ele in test:
        # repeat forever
        print(ele)
