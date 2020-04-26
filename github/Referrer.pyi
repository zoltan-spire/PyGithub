from typing import Any, Dict

class Referrer:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def count(self) -> str: ...
    @property
    def referrer(self) -> str: ...
    @property
    def uniques(self) -> int: ...