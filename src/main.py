from datetime import datetime, timedelta

from src.models import BelfoldiJarat, LegiTarsasag, NemzetkoziJarat
from src.services import FoglalasService


def main() -> None:
    legi_tarsasag = LegiTarsasag("OOP Air")
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B101", "Debrecen", 12990.0))
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B102", "Pecs", 11990.0))
    legi_tarsasag.hozzaad_jarat(NemzetkoziJarat("N201", "Rome", 45990.0))

    service = FoglalasService(legi_tarsasag)

    service.foglal_jegy("B101", "Teszt Elek", datetime.now() + timedelta(hours=2))
    service.foglal_jegy("N201", "Kiss Anna", datetime.now() + timedelta(days=1))

    for foglalas in service.listaz_foglalasok():
        print(
            f"{foglalas.foglalas_id} | {foglalas.utas_nev} | "
            f"{foglalas.jarat.jaratszam} -> {foglalas.jarat.celallomas}"
        )


if __name__ == "__main__":
    main()
