import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter

eingabe_pdf = "C:/Users/chidi/Desktop/General/Scripten_PDF_trennen/StundenplanLehrpersonen2021.pdf"
ausgabe_ordner = "C:/Users/chidi/Desktop/General/Scripten_PDF_trennen/Ausgabe"
os.makedirs(ausgabe_ordner, exist_ok=True)

reader = PdfReader(eingabe_pdf)
plumber_pdf = pdfplumber.open(eingabe_pdf)

for i, (seite_pdf, seite_plumber) in enumerate(zip(reader.pages, plumber_pdf.pages), start=1):
    text = seite_plumber.extract_text()
    name = None

    if text:
        zeilen = text.split('\n')
        if len(zeilen) >= 3:
            dritte_zeile = zeilen[2].strip()
            worte = dritte_zeile.split()
            if len(worte) >= 3:
                # 2. und 3. Wort zusammennehmen
                name = worte[1] + worte[2]
            elif len(worte) >= 2:
                name = worte[1]

    if not name:
        name = f"Seite_{i:03}"

    # Ungültige Zeichen entfernen
    name = re.sub(r"[^\w\-]", "", name)

    writer = PdfWriter()
    writer.add_page(seite_pdf)
    datei_pfad = os.path.join(ausgabe_ordner, f"{name}.pdf")

    with open(datei_pfad, "wb") as f:
        writer.write(f)

    print(f"Seite {i} gespeichert als: {name}.pdf")

print("Fertig!")