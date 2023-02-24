# zoterOPhotosImport.py

import os

base_folder = "/home/jenner/tosync/photos-to-process"

print("zoteroPhotosImport.py")

# if the folder does not exist, exit with an error

if not os.path.isdir(base_folder):
  print(f"{base_folder} does not exist.\nexiting...")
  exit()

# glob the individual files in base_folder
# for each file,
#   
# glob the folders in base_folder
# for each folder, 
#   get the citekey
#   parse the citekey
#   rename all the contained files
