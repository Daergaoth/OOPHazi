from .jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float) -> None:
        super().__init__(jaratszam, celallomas, jegyar)
