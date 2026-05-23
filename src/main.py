from src.models import BelfoldiJarat, LegiTarsasag, NemzetkoziJarat
from src.services import FoglalasService
from src.ui.cli_menu import CLIMenu


def main() -> None:
    legi_tarsasag = LegiTarsasag("OOP Air")
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B101", "Debrecen", 12990.0))
    legi_tarsasag.hozzaad_jarat(BelfoldiJarat("B102", "Pecs", 11990.0))
    legi_tarsasag.hozzaad_jarat(NemzetkoziJarat("N201", "Rome", 45990.0))

    service = FoglalasService(legi_tarsasag)

    from datetime import datetime, timedelta

    foglalasok_adatok = [
        ("B101", "Teszt Elek", datetime.now() + timedelta(hours=2)),
        ("N201", "Kiss Anna", datetime.now() + timedelta(days=1)),
        ("B102", "Nagy Petra", datetime.now() + timedelta(days=2)),
        ("B101", "Szabo Janos", datetime.now() + timedelta(days=3)),
        ("N201", "Varga Maria", datetime.now() + timedelta(days=5)),
        ("B102", "Molnar Bela", datetime.now() + timedelta(days=7)),
    ]

    for jaratszam, utas_nev, idopont in foglalasok_adatok:
        service.foglal_jegy(jaratszam, utas_nev, idopont)

    cli = CLIMenu(service)
    cli.run()


if __name__ == "__main__":
    main()
