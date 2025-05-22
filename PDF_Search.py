import os

#cherche le nom en commencant par le dossier actuel
def find_pdf_by_name(filename, start_directory="."):
    
    pdf_filename = filename.lower() + ".pdf" #convertit en minuscule

    for dirpath, _, filenames in os.walk(start_directory): #cherche dans tout les fichiers du pc
        for file in filenames:
            if file.lower() == pdf_filename: #compare tt les PDF avec le nom du fichier
                return os.path.join(dirpath, file) #donne le chemin complet du PDF

    return None

def search():
    user_input = input("Enter the PDF name (without extansion) : ").strip()
    pdf_path = find_pdf_by_name(user_input) #cherche et compare avec le fichier donné

    if pdf_path:
        print("PDF founded :", pdf_path)
    else:
        print("No PDF founded")

if __name__ == '__main__':
    search()
