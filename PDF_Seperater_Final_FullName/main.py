import os
import re
from PyPDF2 import PdfReader, PdfWriter
import pdfplumber

# === 1. Read abbreviations from name_list.txt ===
def load_abbreviations(txt_path):
    abbreviations = []
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(txt_path, 'r', encoding='latin1') as f:
            lines = f.readlines()
    for line in lines:
        if line.strip():
            parts = re.split(r'\t+', line.strip())
            abbreviation = parts[0].strip().lower()
            abbreviations.append(abbreviation)
    return abbreviations

# === 2. Split PDF page by page and name them using the first word of the 3rd line ===
def split_pdf_by_page(input_pdf, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    reader = PdfReader(input_pdf)

    with pdfplumber.open(input_pdf) as pdf:
        for i, (page, text_page) in enumerate(zip(reader.pages, pdf.pages)):
            writer = PdfWriter()
            writer.add_page(page)

            text = text_page.extract_text()
            filename = f"page_{i+1:03}"  # default name if no text found

            if text:
                lines = text.strip().split('\n')
                if len(lines) >= 3:
                    third_line = lines[2]
                    words = third_line.strip().split()
                    if len(words) >= 1:
                        filename = words[1]+words[2]

            output_path = os.path.join(output_dir, f"{filename}.pdf")

            with open(output_path, "wb") as f:
                writer.write(f)

            print(f"{filename}.pdf created.")

    print(f"{len(reader.pages)} pages successfully separated.\n")

# === 3. Merge single PDFs based on abbreviation list ===
def merge_pdfs_from_list(folder, abbreviation_list, merged_output):
    writer = PdfWriter()
    for code in abbreviation_list:
        file_path = os.path.join(folder, f"{code}.pdf")
        if os.path.exists(file_path):
            reader = PdfReader(file_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"{code}.pdf added.")
        else:
            print(f"{code}.pdf not found, skipped.")
    with open(merged_output, "wb") as f:
        writer.write(f)
    print(f"\n✅ All matching PDFs merged into: '{merged_output}'\n")

## === 4. Delete single-page PDFs (optional cleanup) ===
#def delete_single_page_pdfs(folder):
#    for file in os.listdir(folder):
#        if file.lower().endswith(".pdf"):
#            path = os.path.join(folder, file)
#            try:
#                reader = PdfReader(path)
#                if len(reader.pages) == 1:
#                    os.remove(path)
#                    print(f"{file} deleted (only one page).")
#            except Exception as e:
#                print(f"Could not read {file}: {e}")

# === Main runner ===
if __name__ == "__main__":
    input_pdf_path = "StundenplanLehrpersonen2021.pdf"
    abbreviation_txt_path = "name_list.txt"
    split_output_dir = "OutputPdfs"
    merged_pdf_output = "name_list_merged.pdf"

    # Step 1: Split PDF into single pages named by 3rd line of text
    split_pdf_by_page(input_pdf_path, split_output_dir)

    # Step 2: Load list of abbreviations
    abbreviations = load_abbreviations(abbreviation_txt_path)

    # Step 3: Merge those that match
    merge_pdfs_from_list(split_output_dir, abbreviations, merged_pdf_output)

    # Step 4: Cleanup single-page PDFs
    delete_single_page_pdfs(split_output_dir)

    print("✅ All operations completed successfully.")
