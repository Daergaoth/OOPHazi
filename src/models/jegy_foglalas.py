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
