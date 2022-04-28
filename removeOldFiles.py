"""
Remove old files from the solutions folder and move new files from
submission folder to the solutions folder.

Author: Anjal Gajurel
"""


import os
import shutil
import re
from pathlib import Path


# Select the directory first
dir_name = "C:/Users/anjal/source/repos/sec1/sec1"
test = os.listdir(dir_name)

# Remove the cpp and h files
try:
    for item in test:
        if item.endswith(".h") or item.endswith(".cpp"):
            os.remove(os.path.join(dir_name, item))
            print("removed h and cpp files")
except:
    print("No header or cpp file exists.")

# Remove the folder named Debug
try:
    debug_dir =  dir_name + "/Debug"
    shutil.rmtree(debug_dir)
except:
    print("Debug file does not exist or already deleted")

# Move files from submissions folder to solution folder
# Configure path for source and destination
s_sub_folder = "C:/Users/anjal/source/repos/submissions"
first_sub = os.listdir(s_sub_folder)[0]
source_folder = Path(s_sub_folder + "/" + first_sub)
destination_folder = Path(dir_name)

# Move the files now
for file in source_folder.iterdir():
    file_name = ""
    if re.search('Tokenizer.+', file.stem):
        file_name = 'Tokenizer' + file.suffix
    else:
        file_name = file.stem+file.suffix
    file_move_path = destination_folder.joinpath(file_name)
    file.replace(file_move_path)

# Remove the empty folder once files are moved.
os.rmdir(source_folder)
