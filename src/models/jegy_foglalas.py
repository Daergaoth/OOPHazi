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
        self.__foglalas_id = foglalas_id
        self.__jarat = jarat
        self.__utas_nev = utas_nev
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

    @property
    def foglalas_idopont(self) -> datetime:
        return self.__foglalas_idopont
