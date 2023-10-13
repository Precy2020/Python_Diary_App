from abc import ABC

from data.models.entry import Entry
from data.repositories.entry_repository import EntryRepository


class EntryRepositoryImpl(EntryRepository, ABC):

    def save(self, entry: Entry) -> Entry:
        pass
