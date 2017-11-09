# Medlemslister

Et lite script for å fetche medlemslister for et
gitt semester og lager en .tex fil slik at man enkelt
kan få en PDF.

## Oppsett:
```bash
pip3 install -r requirements.txt
```

## Kjøring:
```bash
python3 memberlists.py "<semester>"
```
Eksempel:
```bash
python3 memberlists.py "v17"
```
Er smart å bygge .tex fila til en PDF ved feks:
```bash
pdftex <semester>.tex
```
