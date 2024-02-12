
import os

import shutil



def organize_files(directory):

    # Dictionary to store file extensions and their corresponding directories

    extensions = {

        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp'],

        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],

        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],

        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],

        'Archives': ['.zip', '.rar', '.tar', '.gz'],

        'Others': []  # Default directory for all other files

    }



    # Create directories if they don't exist

    for folder in extensions.keys():

        if not os.path.exists(os.path.join(directory, folder)):

            os.makedirs(os.path.join(directory, folder))



    # Organize files

    for filename in os.listdir(directory):

        if filename != os.path.basename(__file__):  # Exclude the script itself

            src = os.path.join(directory, filename)

            if os.path.isfile(src):

                file_ext = os.path.splitext(filename)[1]

                moved = False

                for folder, ext_list in extensions.items():

                    if file_ext in ext_list:

                        shutil.move(src, os.path.join(directory, folder, filename))

                        moved = True

                        break

                if not moved:

                    shutil.move(src, os.path.join(directory, 'Others', filename))



if __name__ == "__main__":

    directory = input("Enter directory path to organize files: ")

    organize_files(directory)

    print("Files organized successfully!")



