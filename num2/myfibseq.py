from typing import Iterable, Iterator

class FibSequence(Iterable[int]):
    _end: int

    def __init__(self, end: int) -> None:
        self._end = end

    def __iter__(self) -> Iterator[int]:
        return FibSequenceIterator(self)

class FibSequenceIterator(Iterator[int]):
    _fin: int
    _bef: int
    _af: int
    _times: int

    def __init__(self, fib: FibSequence) -> None:
        self._fin = fib._end
        self._bef = 1
        self._af = 1
        self._times = 0


    def __next__(self) -> int:
        v = self._times
        a = self._bef
        b = self._af
        if v >= self._fin:
            raise StopIteration
        
        self._bef = b
        self._af = a+b
        self._times += 1
        return a

if __name__ == "__main__":
    for v in FibSequence(10):
        print(v)