
import os
import subprocess

def create_and_push_commit_file(repository_path, commit_file_path, commit_message):
    try:
        # Erstelle eine neue Datei commit.py
        with open(commit_file_path, 'w') as commit_file:
            commit_file.write("# Hier kommt der Inhalt Ihrer commit.py-Datei")

        # Füge die Datei zum Index hinzu
        subprocess.run(["git", "add", commit_file_path], cwd=repository_path, check=True)

        # Commit mit der angegebenen Nachricht
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repository_path, check=True)

        # Pushe die Änderungen zum Remote-Repository
        subprocess.run(["git", "push"], cwd=repository_path, check=True)

        print("Erfolgreich gepusht!")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Pushen: {e}")

# Beispielaufruf
repo_path = r"C:\Users\jpl\repository_AutoCommit\Auto-Commit-PG1"
commit_file_path = "commit.py"  # Stellen Sie sicher, dass der Pfad korrekt ist
commit_message = "Neue Datei commit.py erstellt"

# Verwenden Sie den vollständigen Pfad zur commit.py-Datei
full_commit_file_path = os.path.join(repo_path, commit_file_path)

create_and_push_commit_file(repo_path, full_commit_file_path, commit_message)



