from __future__ import annotations


class Clock:

    def __init__(self, hour: int, minute: int):
        self._m = 60 * hour + minute

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._get_hr()}, {self._get_mn()})"

    def __str__(self) -> str:
        return f"{self._get_hr():02}:{self._get_mn():02}"

    def __eq__(self, other: Clock) -> bool:
        return repr(self) == repr(other)

    def __add__(self, minutes: int) -> Clock:
        self._m += minutes
        return self

    def __sub__(self, minutes: int) -> Clock:
        self._m -= minutes
        return self

    def _get_mn(self) -> int:
        return self._m % 60

    def _get_hr(self) -> int:
        return self._m // 60 % 24