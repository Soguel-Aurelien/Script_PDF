# pip install pypdf

import os
from pypdf import PdfReader

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
