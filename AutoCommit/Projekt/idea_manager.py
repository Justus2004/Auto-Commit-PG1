import os


def idee_ziehen():
    dateipfad = 'AutoCommit\Projekt\ideas.txt'
    with open(dateipfad, 'r') as datei:
        zeilen = datei.readlines()
        
    # Die erste Zeile entfernen und am Ende der Liste hinzufügen
    if zeilen:
        erste_zeile = zeilen.pop(0)
        zeilen.append(erste_zeile)

    # Modifizierten Inhalt zurück in die Datei schreiben
    with open(dateipfad, 'w') as datei:
        datei.writelines(zeilen)
    
    return erste_zeile# idea_manager.py