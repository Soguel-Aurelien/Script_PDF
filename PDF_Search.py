import os

def find_pdf_by_name(filename, directory="."): # cherche le pdf mais seulement ds le repertoire actuel
 
    # Fait le nom du fichier en ajoutant l'extansion
    pdf_filename = filename + ".pdf"
    # On combine le répertoire avec le nom du fichier pour obtenir le chemin complet
    pdf_path = os.path.join(directory, pdf_filename)
    
    # Vérifie le fichier
    if os.path.isfile(pdf_path):
        return pdf_path
    else:
        return None

def search():
    # User Input
    user_input = input("Enter a 4 letters visan (low case): ").strip()
    
    # 4 minuscules
    if len(user_input) != 4 or not user_input.islower():
        print("Error : Please enter a 4 letter visa.")
        return
    
    # Recherche le pdf
    pdf_path = find_pdf_by_name(user_input)
    
    if pdf_path:
        print("PDF find :", pdf_path)
        
    else:
        print("No PDF found!.")

if __name__ == '__main__':
    search()
