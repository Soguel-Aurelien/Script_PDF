import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
# Namen Suchen / export split pdf
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

# Suchfunktion 

# Mergefunktion 
 
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pfad_liste, ausgabe_datei):
    writer = PdfWriter()

    for pdf_pfad in pfad_liste:
        reader = PdfReader(pdf_pfad)
        for seite in reader.pages:
            writer.add_page(seite)

    with open(ausgabe_datei, "wb") as f:
        writer.write(f)

    print(f"Merge fertig! Datei gespeichert als: {ausgabe_datei}")



merge_pdfs(****gefundene Pfade hier:**** "C:/Users/chidi/Desktop/General/Scripten_PDF_trennen/Informatiklehrer.pdf")

# Löschfunktion 
# "pip install pypdf" in cmd (Windows) oder bash (Linux) ausführen
# Importiert die benötigten Module
import os
from pypdf2 import PdfReader

# Pfad zum Ordner mit den PDF-Dateien
ordner = "C:\\Users\\scher\\Desktop\\PDF_PowerShell\\PDF_deleteTest"

# Alle PDF-Dateien im Ordner durchgehen
for datei in os.listdir(ordner):
    if datei.lower().endswith(".pdf"):
        pfad = os.path.join(ordner, datei)
        try:
            reader = PdfReader(pfad)
            seiten = len(reader.pages)
            if seiten == 1:
                print(f"Lösche: {datei} (Grund: nicht zussamengefügt)")
                os.remove(pfad)  # <-- tatsächliches Löschen
        except Exception as e:
            print(f"Fehler bei {datei}: {e}")