from datetime import datetime

from .jarat import Jarat


class JegyFoglalas:
    def __init__(
        self,
        foglalas_id: str,
        jarat: Jarat,
        utas_nev: str,
        foglalas_idopont: datetime,
    ) -> None:
        if not foglalas_id or not foglalas_id.strip():
            raise ValueError("A foglalas azonosito nem lehet ures.")
        if not isinstance(jarat, Jarat):
            raise TypeError("A jarat mezonek Jarat peldanynak kell lennie.")
        if not utas_nev or not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet ures.")
        if not isinstance(foglalas_idopont, datetime):
            raise TypeError("A foglalas idopontjanak datetime tipusunak kell lennie.")
        self.__foglalas_id = foglalas_id.strip()
        self.__jarat = jarat
        self.__utas_nev = utas_nev.strip()
        self.__foglalas_idopont = foglalas_idopont

    @property
    def foglalas_id(self) -> str:
        return self.__foglalas_id

    @property
    def jarat(self) -> Jarat:
        return self.__jarat

    @property
    def utas_nev(self) -> str:
        return self.__utas_nev

    @utas_nev.setter
    def utas_nev(self, ertek: str) -> None:
        if not ertek or not ertek.strip():
            raise ValueError("Az utas neve nem lehet ures.")
        self.__utas_nev = ertek.strip()

    @property
    def foglalas_idopont(self) -> datetime:
        return self.__foglalas_idopont
