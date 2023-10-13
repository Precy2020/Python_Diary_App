from data.models.entry import Entry


class Diary:
    identity: int
    username: str
    password: str
    is_locked: str
    entries: Entry = []

    def get_id(self) -> int:
        return self.identity

    def set_id(self, identity: int) -> None:
        self.identity = identity

    def get_username(self) -> str:
        return self.username

    def set_username(self, username: str) -> None:
        self.username = username

    def get_password(self) -> str:
        return self.password

    def set_password(self, password: str) -> None:
        self.password = password

    def get_is_locked(self) -> str:
        return self.is_locked

    def set_is_locked(self, is_locked):
        self.is_locked = is_locked
