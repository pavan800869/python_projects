from typing import Any


class Dictionary(dict):
    def __getattribute__(self, item) -> Any:
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)
        