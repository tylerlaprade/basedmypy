# builtins stub used in for statement test cases

from abc import ABCMeta, abstractmethod
from typing import Generator, Generic, Iterable, Iterator, TypeVar

t = TypeVar("t")

class object:
    def __init__(self) -> None:
        pass

class type:
    pass

class tuple(Generic[t]):
    def __iter__(self) -> Iterator[t]:
        pass

class function:
    pass

class bool:
    pass

class int:
    pass  # for convenience

class str:
    pass  # for convenience

class list(Iterable[t], Generic[t]):
    def __iter__(self) -> Iterator[t]:
        pass
