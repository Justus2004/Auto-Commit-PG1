
import os
import subprocess
class Push:
    def create_and_push_commit_file(temp, commit_message):
        commit_file_path = temp+".py"
        try:
            # Erstelle eine neue Datei commit.py
            with open(commit_file_path, 'w') as commit_file:
                commit_file.write("# Hier kommt der Inhalt Ihrer commit.py-Datei")

            # Füge die Datei zum Index hinzu
            subprocess.run(["git", "add", commit_file_path], cwd="AutoCommit\Projekt", check=True)

            # Commit mit der angegebenen Nachricht
            subprocess.run(["git", "commit", "-m", commit_message], cwd="AutoCommit\Projekt", check=True)

            # Pushe die Änderungen zum Remote-Repository
            subprocess.run(["git", "push"], cwd="AutoCommit\Projekt", check=True)

            print("Erfolgreich gepusht!")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Pushen: {e}")




