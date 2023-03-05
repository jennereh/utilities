# interactiveAlbuminfo.py
# given a list of folders otherwise ready for zoteroPhotosImport.py
# prompt for albuminfo for each

import os, glob

print("interactiveAlbuminfo.py")

base_folder = '/home/jenner/tosync/photos-to-process'

# get in the right dir
if not os.path.isdir(base_folder):
  print(f"{base_folder} does not exist.\nexiting...")
  input("Press [Enter] to continue.")
  exit()
else:
  os.chdir(base_folder)

# get the list of folders

foldersList = glob.glob("*", recursive=False)

for f in foldersList:

    if os.path.isfile(f"{f}/albuminfo")

# if an albuminfo exists
#   if it has a title, display it with y/n to update
#       if yes, prompt for date
#   if it does not have a title
#       if no, prompt for title then date


