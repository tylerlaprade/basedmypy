from typing import Callable, Type

def with_metaclass(mcls: Type[type], *args: type) -> type:
    pass

def add_metaclass(mcls: Type[type]) -> Callable[[type], type]:
    pass
