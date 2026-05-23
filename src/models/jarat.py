from abc import ABC


class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float) -> None:
        if not jaratszam or not jaratszam.strip():
            raise ValueError("A jaratszam nem lehet ures.")
        if not celallomas or not celallomas.strip():
            raise ValueError("A celallomas nem lehet ures.")
        if jegyar <= 0:
            raise ValueError("A jegyar pozitiv szam kell legyen.")
        self.__jaratszam = jaratszam.strip()
        self.__celallomas = celallomas.strip()
        self.__jegyar = jegyar

    @property
    def jaratszam(self) -> str:
        return self.__jaratszam

    @property
    def celallomas(self) -> str:
        return self.__celallomas

    @celallomas.setter
    def celallomas(self, ertek: str) -> None:
        if not ertek or not ertek.strip():
            raise ValueError("A celallomas nem lehet ures.")
        self.__celallomas = ertek.strip()

    @property
    def jegyar(self) -> float:
        return self.__jegyar

    @jegyar.setter
    def jegyar(self, ertek: float) -> None:
        if ertek <= 0:
            raise ValueError("A jegyar pozitiv szam kell legyen.")
        self.__jegyar = ertek
