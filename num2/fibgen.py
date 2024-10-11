class FibGenerator:
    _num: int
    def __init__(self, num: int):
        self._num = num

    def __iter__(self):
        i = 0
        j = 1
        times = self._num
        while times > 0:
            yield j
            tmp = j
            j = i + j
            i = tmp
            times -= 1


if __name__=="__main__":
    for v in FibGenerator(10):
        print(v)