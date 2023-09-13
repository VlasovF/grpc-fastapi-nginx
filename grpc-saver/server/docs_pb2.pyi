from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Point(_message.Message):
    __slots__ = ["lat", "lon"]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ...) -> None: ...

class SaveDocumentRequest(_message.Message):
    __slots__ = ["article_id", "text", "title", "date", "lang", "locations", "semantic_vector", "keywords", "entities", "themes"]
    ARTICLE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VECTOR_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    article_id: int
    text: str
    title: str
    date: str
    lang: str
    locations: _containers.RepeatedCompositeFieldContainer[Point]
    semantic_vector: _containers.RepeatedScalarFieldContainer[float]
    keywords: _containers.RepeatedScalarFieldContainer[str]
    entities: _containers.RepeatedScalarFieldContainer[str]
    themes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, article_id: _Optional[int] = ..., text: _Optional[str] = ..., title: _Optional[str] = ..., date: _Optional[str] = ..., lang: _Optional[str] = ..., locations: _Optional[_Iterable[_Union[Point, _Mapping]]] = ..., semantic_vector: _Optional[_Iterable[float]] = ..., keywords: _Optional[_Iterable[str]] = ..., entities: _Optional[_Iterable[str]] = ..., themes: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class SaveDocumentReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
