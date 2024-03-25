from .base import (
    SchemaStrategy,
    TypedSchemaStrategy
)
from .scalar import (
    Typeless,
    Null,
    Boolean,
    Number,
    String
)
from .array import List, Tuple, StreamingList
from .object import Object, StreamingObject

BASIC_SCHEMA_STRATEGIES = (
    Null,
    Boolean,
    Number,
    String,
    List,
    Tuple,
    Object,
    StreamingObject,
    StreamingList,
)

__all__ = (
    'SchemaStrategy',
    'TypedSchemaStrategy',
    'Null',
    'Boolean',
    'Number',
    'String',
    'List',
    'Tuple',
    'Object',
    'Typeless',
    'BASIC_SCHEMA_STRATEGIES'
)
