import sys
from typing import Callable, ContextManager as ContextManager, Generic, Iterator, TypeVar

_T = TypeVar("_T")

class GeneratorContextManager(ContextManager[_T], Generic[_T]):
    def __call__(self, func: Callable[..., _T]) -> Callable[..., _T]: ...

def contextmanager(
    func: Callable[..., Iterator[_T]]
) -> Callable[..., GeneratorContextManager[_T]]: ...

if sys.version_info >= (3, 7):
    from typing import AsyncContextManager as AsyncContextManager, AsyncIterator
    def asynccontextmanager(
        func: Callable[..., AsyncIterator[_T]]
    ) -> Callable[..., AsyncContextManager[_T]]: ...
