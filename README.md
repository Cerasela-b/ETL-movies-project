# ETL Movies Project

Acesta este un proiect de procesare a datelor despre filme folosind un proces ETL (Extract, Transform, Load). Proiectul utilizează Python și biblioteci de procesare a datelor precum `pandas` pentru a extrage, transforma și încarca datele într-un fișier Excel.

## Descriere

Scopul proiectului este de a prelucra datele despre filme pentru a genera topuri de filme pe baza încasărilor (`box_office`) și bugetului (`budget`) pentru diferite țări. Datele sunt procesate folosind pașii ETL următori:

- **Extract**: Extrage datele dintr-un fișier CSV cu informații despre filme.
- **Transform**: Se efectuează curățarea și transformarea datelor, calculând coloana `bilant` (diferența între încasări și buget).
- **Load**: Datele procesate sunt exportate într-un fișier Excel pentru fiecare țară selectată (ex: USA, UK, South Korea).

## Tehnologii utilizate

- Python 3.x
- pandas
- openpyxl (pentru a salva fișierele Excel)

## Cum să folosești proiectul

1. Clonează proiectul:
   ```bash
   git clone https://github.com/<user>/<repo-name>.git
