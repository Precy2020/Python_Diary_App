from abc import ABC
from typing import Iterable

from data.models.diary import Diary
from data.repositories.diary_repository import DiaryRepository


class DiaryRepositoryImpl(DiaryRepository, ABC):
    __diaries = []

    def save(self, diary: Diary) -> Diary:
        if diary.get_id() == 0:
            self.new_diary(diary)
        else:
            self.update(diary)
            return diary

    def generate_id(self) -> int:
        return self.__diaries.__sizeof__() + 1

    def new_diary(self, diary) -> None:
        diary.set_id(self.generate_id())
        self.__diaries.append(diary)

    def update(self, diary) -> None:
        update_diary: Diary = self.find_by_id(diary.get_id())
        update_diary.set_username(update_diary.get_username())

    def find_by_id(self, identity) -> Diary:
        for diary in self.__diaries:
            if diary.get_id == identity:
                return diary

    def delete(self, identity) -> None:
        self.__diaries.remove(self.find_by_id(identity))

    def find_all(self) -> Iterable[Diary]:
        return self.__diaries

    def size(self) -> int:
        return self.__diaries.__sizeof__()

