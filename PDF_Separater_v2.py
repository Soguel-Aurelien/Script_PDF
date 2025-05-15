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
