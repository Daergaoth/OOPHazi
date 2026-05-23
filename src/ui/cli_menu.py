from datetime import datetime

from src.services import FoglalasService


class CLIMenu:

    def __init__(self, foglalas_service: FoglalasService) -> None:
        if not isinstance(foglalas_service, FoglalasService):
            raise TypeError("A foglalas_service parameternek FoglalasService peldanynak kell lennie.")
        self.service = foglalas_service

    def run(self) -> None:
        print("\n" + "=" * 60)
        print("  REPÜLŐJEGY FOGLALÁSI RENDSZER".center(60))
        print("=" * 60 + "\n")
        
        while True:
            self._show_main_menu()
            choice = input("\nVálassz: ").strip()
            self._handle_main_choice(choice)

    def _show_main_menu(self) -> None:
        print("\n" + "-" * 60)
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("5. Kilépés")
        print("-" * 60)

    def _handle_main_choice(self, choice: str) -> None:
        if choice == "1":
            self._foglal_jegy_menu()
        elif choice == "2":
            self._lemond_foglalas_menu()
        elif choice == "3":
            self._listaz_foglalasok_menu()
        elif choice == "4":
            self._listaz_jaratok_menu()
        elif choice == "5":
            print("\nViszlát!\n")
            exit()
        else:
            print("Érvénytelen választás. Próbálj újra.")
    def _foglal_jegy_menu(self) -> None:
        print("\n" + "=" * 60)
        print("  JEGY FOGLALÁSA".center(60))
        print("=" * 60)

        print("\nElérhető járatok:")
        jaratok = self.service.get_jaratok()
        for idx, jarat in enumerate(jaratok, 1):
            print(f"  {idx}. {jarat.jaratszam:6} -> {jarat.celallomas:15} ({jarat.jegyar:8.0f} Ft)")

        print()
        jaratszam = input("Járatszám (pl. B101): ").strip().upper()
        if not jaratszam:
            print("Járatszám nem lehet üres.")
            return

        utas_nev = input("Utas neve: ").strip()
        if not utas_nev:
            print("Utas neve nem lehet üres.")
            return

        print("\nFoglalás időpontja (opcionális, YYYY-MM-DD HH:MM formátum):")
        print("  (Hagyja üresen, ha most szeretne foglalni)")
        idopont_str = input("Időpont: ").strip()
        
        foglalas_idopont = None
        if idopont_str:
            try:
                foglalas_idopont = datetime.strptime(idopont_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Érvénytelen dátum formátum. Foglalás lemondva.")
                return

        try:
            ar = self.service.foglal_jegy(jaratszam, utas_nev, foglalas_idopont)
            print(f"\nSikeresen foglalva!")
            print(f"   Járat: {jaratszam}")
            print(f"   Utas: {utas_nev}")
            print(f"   Ár: {ar:8.0f} Ft")
        except ValueError as e:
            print(f"\nHiba: {e}")
        except TypeError as e:
            print(f"\nTípus hiba: {e}")

    def _lemond_foglalas_menu(self) -> None:
        print("\n" + "=" * 60)
        print("  FOGLALÁS LEMONDÁSA".center(60))
        print("=" * 60)

        # Foglalások listázása
        foglalasok = self.service.listaz_foglalasok()
        if not foglalasok:
            print("\nNincsenek foglalások.")
            return

        print("\nAktuális foglalások:")
        for idx, fog in enumerate(foglalasok, 1):
            print(
                f"  {idx}. {fog.foglalas_id:6} | {fog.utas_nev:20} | "
                f"{fog.jarat.jaratszam:6} -> {fog.jarat.celallomas:15}"
            )

        print()
        foglalas_id = input("Foglalás azonosítója (pl. F0001): ").strip().upper()
        if not foglalas_id:
            print("Foglalás azonosítója nem lehet üres.")
            return

        # Service meghívása
        try:
            self.service.lemond_foglalas(foglalas_id)
            print(f"\nFoglalás sikeresen lemondva: {foglalas_id}")
        except ValueError as e:
            print(f"\nHiba: {e}")

    def _listaz_foglalasok_menu(self) -> None:
        print("\n" + "=" * 60)
        print("  FOGLALÁSOK LISTÁZÁSA".center(60))
        print("=" * 60)

        foglalasok = self.service.listaz_foglalasok()
        
        if not foglalasok:
            print("\nNincsenek foglalások.")
            return

        print(f"\nÖsszes foglalás ({len(foglalasok)} db):\n")
        print(
            f"{'ID':6} | {'Utas':20} | {'Járat':6} | {'Cél':15} | {'Ár':8} | {'Foglalás időpontja':20}"
        )
        print("-" * 105)
        
        for fog in foglalasok:
            print(
                f"{fog.foglalas_id:6} | {fog.utas_nev:20} | "
                f"{fog.jarat.jaratszam:6} | {fog.jarat.celallomas:15} | "
                f"{fog.jarat.jegyar:8.0f} | {fog.foglalas_idopont.strftime('%Y-%m-%d %H:%M'):20}"
            )
        
        print(f"\nÖsszes foglalás ára: {sum(fog.jarat.jegyar for fog in foglalasok):8.0f} Ft")

    def _listaz_jaratok_menu(self) -> None:
        print("\n" + "=" * 60)
        print("  JÁRATOK LISTÁZÁSA".center(60))
        print("=" * 60)

        jaratok = self.service.get_jaratok()
        
        if not jaratok:
            print("\n⚠️  Nincsenek elérhető járatok.")
            return

        print(f"\nÖsszes elérhető járat ({len(jaratok)} db):\n")
        print(f"{'Járatszám':10} | {'Típus':15} | {'Célállomás':15} | {'Ár':8}")
        print("-" * 60)
        
        for jarat in jaratok:
            jarattipus = type(jarat).__name__.replace("Jarat", "")
            print(
                f"{jarat.jaratszam:10} | {jarattipus:15} | {jarat.celallomas:15} | "
                f"{jarat.jegyar:8.0f} Ft"
            )
