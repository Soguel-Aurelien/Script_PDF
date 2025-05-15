import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
# Namen Suchen / export split pdf
eingabe_pdf = "C:/StundenplanLehrpersonen2021.pdf"
ausgabe_ordner = "C:/Ausgabeordner_pdf"
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
# Suchfunktion  
import os #Klasör oluşturma ve dosya yolları için.
from PyPDF2 import PdfReader, PdfWriter #PDF’i okumak ve sayfa sayfa kaydetmek için.
import pdfplumber #PDF dosyasını açar, metin okur.

# Giriş PDF dosyası
input_pdf = "StundenplanLehrpersonen2021.pdf"

# Çıktı klasörü
output_folder = "OutputPdfs"

# Eğer klasör yoksa oluştur
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# PyPDF2 ile PDF'i oku (sayfaları bölmek için)
reader = PdfReader(input_pdf) #PDF’i sayfa sayfa okuyacağız (ama metin içeriğini değil).

# pdfplumber ile de metni alacağız. Her sayfanın içindeki metni pdfplumber ile okuyacağız.
with pdfplumber.open(input_pdf) as pdf: #with bloğu dosyayı açar ve iş bitince otomatik kapatır.

    # Her sayfa için döngü
    #page: PDF sayfasının içeriği (yazdırmak için).
    #text_page: Metin içeriği (başlık çıkarmak için).
    #enumerate: Sayfa numarasını (i) verir.
    for i, (page, text_page) in enumerate(zip(reader.pages, pdf.pages)): #zip(...), iki listeyi eşleştirir. Aynı uzunlukta iki dizin varsa, her ikisinden aynı anda öğe alırsın.
        writer = PdfWriter() #Pdf dosyasi olusturur
        writer.add_page(page) #bir sayfa ekler

        # Sayfanın metnini al
        text = text_page.extract_text() #Sayfa metnini alır.
        third_line = text.strip().split('\n')[2]  # ücuncü satırı al
        visa = third_line.strip().split()[0]  # İlk kelimeyi başlık olarak kullan

        newPdfFileName = f"{visa}.pdf"
        newPdfFilePath = os.path.join(output_folder, newPdfFileName) #Yeni PDF dosyasını output_folder içinde newPdfFileName ile kaydeder.
         
        with open(newPdfFilePath, "wb") as f: #Write Binary pdf ye uygundur. with kullanımı sayesinde dosya açık unutulmaz.
            writer.write(f)

        print(f"{newPdfFileName} created.") #Hangi dosyanın üretildiğini kullanıcıya bildirir.

print(f"{len(reader.pages)} pages sucessfully separated.") #sonuc mesaji
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





# Löschfunktion 
# "pip install pypdf" in cmd (Windows) oder bash (Linux) ausführen
# Importiert die benötigten Module
import os
from PyPDF2 import PdfReader

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

