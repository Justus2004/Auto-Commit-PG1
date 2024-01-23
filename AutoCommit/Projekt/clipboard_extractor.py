# clipboard_extractor.py
import re
import pyperclip
from idea_manager import IdeaManager

class ClipboardExtractor:
    @staticmethod
    def extract_code(text):
        # Definieren Sie einen regulären Ausdruck, um Code zu erkennen (z.B. beginnt mit "```" und endet mit "```")
        code_pattern = r'```([\s\S]*?)```'

        # Finden Sie alle Übereinstimmungen des regulären Ausdrucks im Text
        code_matches = re.findall(code_pattern, text)

        # Rückgabe der extrahierten Code-Abschnitte
        return code_matches

    @staticmethod
    def extract_code_from_clipboard():
        # Text aus der Zwischenablage kopieren
        clipboard_text = pyperclip.paste()

        # Extrahieren Sie den Code aus dem kopierten Text
        extracted_code = ClipboardExtractor.extract_code(clipboard_text)

        # Drucken Sie den extrahierten Code
        for code_block in extracted_code:
            print("Extrahierter Code:")
            print(code_block)

        # Speichern Sie den extrahierten Code in einer neuen Python-Datei
        ClipboardExtractor.save_code_to_file(extracted_code)

    @staticmethod
    def save_code_to_file(code_blocks,file_name):
        # Erstellen Sie eine neue Datei mit einem eindeutigen Namen

        with open(file_name+".py", "w") as file:
            # Schreiben Sie den extrahierten Code in die Datei
            for code_block in code_blocks:
                file.write(code_block)
                file.write("\n\n")

        print(f"Extrahierter Code wurde in der Datei '{file_name}' gespeichert.")
        return file

if __name__ == "__main__":
    ClipboardExtractor.extract_code_from_clipboard()
