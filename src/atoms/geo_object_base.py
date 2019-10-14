from typing import Any
from abc import ABC, abstractmethod


class GeoObject(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
        return ""

    @abstractmethod
    def get_num_dimensions(self) -> int:
        pass

    @abstractmethod
    def get_smallest_containing_box(self) -> Any:
        pass

    def __repr__(self) -> str:
        return self.get_name()
