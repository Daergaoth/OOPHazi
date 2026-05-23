from .jarat import Jarat


class LegiTarsasag:
    def __init__(self, nev: str) -> None:
        self.__nev = nev
        self.__jaratok: list[Jarat] = []

    @property
    def nev(self) -> str:
        return self.__nev

    @property
    def jaratok(self) -> list[Jarat]:
        return list(self.__jaratok)

    def hozzaad_jarat(self, jarat: Jarat) -> None:
        self.__jaratok.append(jarat)
