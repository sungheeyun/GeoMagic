from abc import ABC, abstractmethod


class GeoObject(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
        return ""

    @abstractmethod
    def get_num_dimensions(self) -> int:
        pass

    def __repr__(self) -> str:
        return self.get_name()
