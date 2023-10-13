from abc import ABC, abstractmethod
from typing import Iterable

from data.models.diary import Diary


class DiaryRepository(ABC):
    @abstractmethod
    def save(self, diary: Diary) -> Diary:
        pass

    @abstractmethod
    def find_by_id(self, identity) -> Diary:
        pass

    @abstractmethod
    def delete(self, identity) -> None:
        pass

    @abstractmethod
    def find_all(self) -> Iterable[Diary]:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
