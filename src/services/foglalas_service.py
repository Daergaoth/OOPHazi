from datetime import datetime

from src.models.jarat import Jarat
from src.models.jegy_foglalas import JegyFoglalas
from src.models.legi_tarsasag import LegiTarsasag


class FoglalasService:
    def __init__(self, legi_tarsasag: LegiTarsasag) -> None:
        if not isinstance(legi_tarsasag, LegiTarsasag):
            raise TypeError("A legi_tarsasag parametemek LegiTarsasag peldanynak kell lennie.")
        self.__legi_tarsasag = legi_tarsasag
        self.__foglalasok: list[JegyFoglalas] = []
        self.__kovetkezo_id = 1

    def get_jaratok(self) -> list[Jarat]:
        return self.__legi_tarsasag.jaratok

    def foglal_jegy(
        self,
        jaratszam: str,
        utas_nev: str,
        foglalas_idopont: datetime | None = None,
    ) -> float:
        if not isinstance(jaratszam, str) or not jaratszam.strip():
            raise ValueError("A jaratszam nem lehet ures.")

        if not isinstance(utas_nev, str) or not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet ures.")

        if foglalas_idopont is not None:
            if not isinstance(foglalas_idopont, datetime):
                raise TypeError("A foglalas idopontjanak datetime tipusunak kell lennie.")
            if foglalas_idopont < datetime.now():
                raise ValueError("A foglalas idopontja nem lehet a multban.")
        idopont = foglalas_idopont or datetime.now()

        jarat = self.__keres_jarat(jaratszam.strip())
        if jarat is None:
            raise ValueError(f"Nem letezik jarat ezzel a szammal: '{jaratszam}'.")

        foglalas_id = f"F{self.__kovetkezo_id:04d}"
        self.__kovetkezo_id += 1
        foglalas = JegyFoglalas(foglalas_id, jarat, utas_nev.strip(), idopont)
        self.__foglalasok.append(foglalas)
        return jarat.jegyar

    def lemond_foglalas(self, foglalas_id: str) -> None:
        if not isinstance(foglalas_id, str) or not foglalas_id.strip():
            raise ValueError("A foglalas azonosito nem lehet ures.")

        for index, foglalas in enumerate(self.__foglalasok):
            if foglalas.foglalas_id == foglalas_id.strip():
                del self.__foglalasok[index]
                return

        raise ValueError(f"Nem letezik foglalas ezzel az azonositoval: '{foglalas_id}'.")

    def listaz_foglalasok(self) -> list[JegyFoglalas]:
        return list(self.__foglalasok)

    def __keres_jarat(self, jaratszam: str) -> Jarat | None:
        for jarat in self.__legi_tarsasag.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None
