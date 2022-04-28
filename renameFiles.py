from pathlib import Path
import os

our_files = Path("C:/Users/anjal/source/repos/submissions")


for file in our_files.iterdir():

    if file.is_file() and file.stem != ".DS_Store":
        directory = file.parent
        extension = file.suffix

        old_name = file.stem

        per_name = ""
        status = ""
        number1 = ""
        number2 = ""
        new_name = ""


        # Spot Late files and still rename based on it
        try:
            per_name, number1, number2, new_name = old_name.split('_')

        except ValueError:
            per_name, status, number1, number2, new_name = old_name.split('_')

        # Rename the file name
        new_file = f'{new_name}{extension}'

        new_path = ""

        # Check if the submission is Late
        if status != "LATE":
            new_path = our_files.joinpath(per_name)
        else:
            new_per_name = f'{per_name}_{status}'
            new_path = our_files.joinpath(new_per_name)

        # Check if the folder exists
        if not new_path.exists():
            new_path.mkdir()

        new_file_path = new_path.joinpath(new_file)

        file.replace(new_file_path)


