from datetime import datetime, timedelta

from src.models import BelfoldiJarat, LegiTarsasag, NemzetkoziJarat
from src.services import FoglalasService


def main() -> None:
    # Legitarsasag es jaratok letrehozasa
    legi_tarsasag = LegiTarsasag("OOP Air")
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B101", "Debrecen", 12990.0))
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B102", "Pecs", 11990.0))
    legi_tarsasag.hozzaad_jarat(NemzetkoziJarat("N201", "Rome", 45990.0))

    service = FoglalasService(legi_tarsasag)

    print("=== ELOKESZITES: 6 foglalasok betoltese ===\n")

    foglalasok_adatok = [
        ("B101", "Teszt Elek", datetime.now() + timedelta(hours=2)),
        ("N201", "Kiss Anna", datetime.now() + timedelta(days=1)),
        ("B102", "Nagy Petra", datetime.now() + timedelta(days=2)),
        ("B101", "Szabo Janos", datetime.now() + timedelta(days=3)),
        ("N201", "Varga Maria", datetime.now() + timedelta(days=5)),
        ("B102", "Molnar Bela", datetime.now() + timedelta(days=7)),
    ]

    for jaratszam, utas_nev, idopont in foglalasok_adatok:
        ar = service.foglal_jegy(jaratszam, utas_nev, idopont)
        print(f"Foglalva: {utas_nev:20} -> {jaratszam} ({ar} Ft)")

    print("\n=== OSSZES FOGLALASOK ===\n")
    for foglalas in service.listaz_foglalasok():
        print(
            f"{foglalas.foglalas_id:6} | {foglalas.utas_nev:20} | "
            f"{foglalas.jarat.jaratszam:6} -> {foglalas.jarat.celallomas:15} | "
            f"Ar: {foglalas.jarat.jegyar:8.0f} Ft"
        )


if __name__ == "__main__":
    main()
