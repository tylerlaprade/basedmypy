from typing import Callable, Optional

from mypy.plugin import AttributeContext, Plugin
from mypy.types import Instance, Type


class AttrPlugin(Plugin):
    def get_attribute_hook(self, fullname: str) -> Optional[Callable[[AttributeContext], Type]]:
        if fullname == "m.Signal.__call__":
            return signal_call_callback
        return None


def signal_call_callback(ctx: AttributeContext) -> Type:
    if isinstance(ctx.type, Instance):
        return ctx.type.args[0]
    return ctx.default_attr_type


def plugin(version):
    return AttrPlugin
