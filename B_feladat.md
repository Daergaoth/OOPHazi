# Repülőjegy Foglalási Rendszer

Ez a projekt egy egyszerű repülőjegy foglalási rendszert valósít meg, ahol járatokra lehet jegyet foglalni, lemondani a foglalást, és megtekinteni az aktuális foglalások listáját.

## Általános elvárások

- Pythonban készítsétek a vizsgafeladatot.
- A kész projektet töltsétek fel a saját GitHub repositorytokban. 
  - Figyeljetek rá hogy a repó láthatósága PUBLIC legyen!
- A feladatot beadni a Neptunban a "Kötelező project feladat" elnevezéső feladatban kell. 
  - Készíts egy NEPTUNKOD.docx fájlt, amibe másold bele az előbbi pontban írt github repository linkjét. Ezt a fájlt töltsd fel!
- **Határidő: 2026.05.24 23:59:59.**
- Elküldés előtt tegyétek meg a következőket:
  - Egy browser incognito ablakában nézzétek meg az elküldendő GitHub repositoryt (látható, fent van az utolsó commit is).
  - Clone-ozzátok ki a repositoryt PyCharm-ban, és nézzétek meg, hogy futtatható-e (így fogom én is tesztelni, el kell induljon a projekt, hogy értékelni tudjam).
- Elevator pitch videó készítése
  - Rövid 2 nagyon max 3 perces videó ahol bemutatjátok az elkészült project feladatot. 

## Fő osztályok

- **Járat (absztrakt osztály):** Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
- **BelföldiJarat:** Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
- **NemzetkoziJarat:** Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
- **LégiTársaság:** Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
- **JegyFoglalás:** A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

## Funkciók

- **Jegy foglalása:** A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
- **Foglalás lemondása:** A felhasználó lemondhatja a meglévő foglalást.
- **Foglalások listázása:** Az összes aktuális foglalás listázása.

## További elvárt funkciók
- Ahol csak lehet használj non-public attribútumokat, szükség esetén írj hozzá getter/setter-t.
- Használj hibakezelést.

## Adatvalidáció

- Ellenőrzi, hogy a járat elérhető-e foglalásra, és hogy a foglalás időpontja érvényes-e.
- Biztosítja, hogy csak létező foglalásokat lehessen lemondani.

## Felhasználói interfész

- Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
  - Jegy foglalása
  - Foglalás lemondása
  - Foglalások listázása

## Előkészítés

A rendszer indulásakor egy légitársaság, 3 járat és 6 foglalás előre be van töltve a rendszerbe, így a felhasználó azonnal használatba veheti a rendszert.
