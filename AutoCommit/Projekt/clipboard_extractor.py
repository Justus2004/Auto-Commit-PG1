# clipboard_extractor.py
import re
import pyperclip

def extract_code(text):
    # Definieren Sie einen regulären Ausdruck, um Code zu erkennen (z.B. beginnt mit "```" und endet mit "```")
    code_pattern = r'```([\s\S]*?)```'

    # Finden Sie alle Übereinstimmungen des regulären Ausdrucks im Text
    code_matches = re.findall(code_pattern, text)

    # Rückgabe der extrahierten Code-Abschnitte
    return code_matches
    
def extract_code_from_clipboard(file_name):
    # Text aus der Zwischenablage kopieren
    clipboard_text = pyperclip.paste()

    # Extrahieren Sie den Code aus dem kopierten Text
    extracted_code = extract_code(clipboard_text)

    # Speichern Sie den extrahierten Code in einer neuen Python-Datei
    save_code_to_file(extracted_code,file_name)
        
def save_code_to_file(code_blocks,file_name):
    # Erstellen Sie eine neue Datei mit einem eindeutigen Namen

    with open(file_name, "w") as file:
        # Schreiben Sie den extrahierten Code in die Datei
        for code_block in code_blocks:
            file.write(code_block)
            file.write("\n\n")
                
    with open(file_name, 'r') as datei:
        zeilen = datei.readlines()
        
    # Die erste Zeile entfernen und am Ende der Liste hinzufügen
    if zeilen:
        zeilen.pop(0)
        
    with open(file_name, 'w') as datei:
        datei.writelines(zeilen)

    print(f"Extrahierter Code wurde in der Datei '{file_name}' gespeichert.")
    return file
