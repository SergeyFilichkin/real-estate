from rest_framework.fields import Field
from rest_framework.serializers import Serializer


def inline_serializer(
    name: str,
    fields: dict[str, Field],
    docstring: str = "",
    **kwargs,
) -> Serializer:
    serializer_class = type(name, (Serializer,), fields)
    serializer_class.__doc__ = docstring
    return serializer_class(**kwargs)
