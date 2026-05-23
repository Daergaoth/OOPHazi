from .jarat import Jarat


class LegiTarsasag:
    def __init__(self, nev: str) -> None:
        if not nev or not nev.strip():
            raise ValueError("A legitarsasag neve nem lehet ures.")
        self.__nev = nev.strip()
        self.__jaratok: list[Jarat] = []

    @property
    def nev(self) -> str:
        return self.__nev

    @nev.setter
    def nev(self, ertek: str) -> None:
        if not ertek or not ertek.strip():
            raise ValueError("A legitarsasag neve nem lehet ures.")
        self.__nev = ertek.strip()

    @property
    def jaratok(self) -> list[Jarat]:
        return list(self.__jaratok)

    def hozzaad_jarat(self, jarat: Jarat) -> None:
        if not isinstance(jarat, Jarat):
            raise TypeError("Csak Jarat peldany adhato hozza.")
        if any(j.jaratszam == jarat.jaratszam for j in self.__jaratok):
            raise ValueError(f"Mar letezik jarat ezzel a szammal: {jarat.jaratszam}")
        self.__jaratok.append(jarat)
