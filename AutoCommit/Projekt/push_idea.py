import os
import subprocess

def create_and_push_commit_file(commit_file_path, commit_message):
    try:
        # Verify if the file exists
        if not os.path.isfile(commit_file_path):
            print(f"Error: File '{commit_file_path}' not found.")
            return

        # Add the file to the Git index
        subprocess.run(["git", "add", commit_file_path], check=True)

        # Commit with the specified message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push the changes to the remote repository
        subprocess.run(["git", "push"], check=True)

        print("Successfully pushed!")
    except subprocess.CalledProcessError as e:
        print(f"Error while pushing: {e}")


