from datetime import datetime

from src.models.jarat import Jarat
from src.models.jegy_foglalas import JegyFoglalas
from src.models.legi_tarsasag import LegiTarsasag


class FoglalasService:
    def __init__(self, legi_tarsasag: LegiTarsasag) -> None:
        self.__legi_tarsasag = legi_tarsasag
        self.__foglalasok: list[JegyFoglalas] = []
        self.__kovetkezo_id = 1

    def foglal_jegy(
        self,
        jaratszam: str,
        utas_nev: str,
        foglalas_idopont: datetime | None = None,
    ) -> float:
        if not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet ures.")

        idopont = foglalas_idopont or datetime.now()
        if idopont < datetime.now():
            raise ValueError("A foglalas idopontja nem lehet a multban.")

        jarat = self.__keres_jarat(jaratszam)
        if jarat is None:
            raise ValueError(f"Nincs ilyen jarat: {jaratszam}")

        foglalas_id = f"F{self.__kovetkezo_id:04d}"
        self.__kovetkezo_id += 1

        foglalas = JegyFoglalas(foglalas_id, jarat, utas_nev, idopont)
        self.__foglalasok.append(foglalas)
        return jarat.jegyar

    def lemond_foglalas(self, foglalas_id: str) -> None:
        for index, foglalas in enumerate(self.__foglalasok):
            if foglalas.foglalas_id == foglalas_id:
                del self.__foglalasok[index]
                return

        raise ValueError(f"Nem letezo foglalas azonosito: {foglalas_id}")

    def listaz_foglalasok(self) -> list[JegyFoglalas]:
        return list(self.__foglalasok)

    def __keres_jarat(self, jaratszam: str) -> Jarat | None:
        for jarat in self.__legi_tarsasag.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None
