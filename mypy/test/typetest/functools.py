from __future__ import annotations

from functools import _lru_cache_wrapper, lru_cache

# use `basedtyping` when we drop python 3.8
from types import FunctionType, MethodType
from typing import TYPE_CHECKING, Callable, Protocol
from typing_extensions import assert_type

from mypy_extensions import Arg

# use `functools.cache` when we drop python 3.8
cache = lru_cache(None)


class A:
    @cache
    def m(self, a: int): ...

    @classmethod
    @cache
    def c(cls, a: int): ...

    @staticmethod
    @cache
    def s(a: int): ...


@cache
def f(a: int): ...


if TYPE_CHECKING:
    from functools import _HashCallable, _LruCacheWrapperBase, _LruCacheWrapperMethod

    a = A()
    ExpectedFunction = _LruCacheWrapperBase[Callable[[Arg(int, "a")], None]]
    ExpectedMethod = _LruCacheWrapperMethod[Callable[[Arg(int, "a")], None]]
    ExpectedMethodNone = _LruCacheWrapperMethod["() -> None"]
    assert_type(a.m, ExpectedMethod)
    assert_type(a.c, ExpectedMethod)
    # this is wrong, it shouldn't eat the `a` argument, but this is because of mypy `staticmethod` special casing
    assert_type(a.s, ExpectedMethodNone)
    assert_type(a.s, MethodType & (_LruCacheWrapperBase[Callable[[Arg(int, "a")], None]] | _HashCallable))  # type: ignore[assert-type]
    assert_type(f.__get__(1), ExpectedMethodNone)
