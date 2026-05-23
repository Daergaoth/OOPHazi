from abc import ABC


class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float) -> None:
        self.__jaratszam = jaratszam
        self.__celallomas = celallomas
        self.__jegyar = jegyar

    @property
    def jaratszam(self) -> str:
        return self.__jaratszam

    @property
    def celallomas(self) -> str:
        return self.__celallomas

    @property
    def jegyar(self) -> float:
        return self.__jegyar
