
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