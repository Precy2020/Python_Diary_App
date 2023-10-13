from abc import ABC, abstractmethod
from typing import Iterable

from data.models.entry import Entry


class EntryRepository(ABC):

    @abstractmethod
    def save(self, entry: Entry) -> Entry:
        pass

    @abstractmethod
    def delete(self, owner_name: str, title: str) -> None:
        pass

    @abstractmethod
    def find_by_id(self, identity: int) -> Entry:
        pass

    @abstractmethod
    def find_all(self) -> Iterable[Entry]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def find_by_username(self) -> Entry:
        pass
