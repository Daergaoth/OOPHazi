# OOP Hazi - Repulojegy Foglalasi Rendszer

Ez a projekt egy egyszeru CLI alapu repulojegy foglalasi rendszer.

## Rendszerigeny

- Python 3.10 vagy ujabb
- Git (clone-hoz)

## Gyors inditas (friss clone utan)

### 1) Repository klonozasa

```powershell
git clone <A_SAJAT_REPO_URL>
cd <A_REPO_MAPPANEVE>
```

### 2) Virtualis kornyezet letrehozasa

```powershell
python -m venv .venv
```

### 3) Virtualis kornyezet aktivalasa

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4) Fuggosegek telepitese

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Megjegyzes: jelenleg nincs kulso pip fuggoseg, de a parancsot erdemes megtartani.

### 5) Program inditasa

```powershell
python -m src.main
```

## CLI menu funkciok

A program indulasa utan az alabbi menupontok erhetoek el:

1. Jegy foglalasa
2. Foglalas lemondasa
3. Foglalasok listazasa
4. Jaratok listazasa
5. Kilepes
