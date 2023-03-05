# interactiveAlbuminfo.py
# given a list of folders otherwise ready for zoteroPhotosImport.py
# prompt for albuminfo for each
#
# --------------------------------------------
# --- hanni20090915lastweekyuma
# --- albuminfo
# [t] title: Better Title
# [p] prev: 
# [n] next: 
#     additional_field:
#     another_field: 
# [o] open the file for hand-editing
# [x] everything looks good
# --------------------------------------------

import os, glob

mainKeys = ["title", "prev", "next"]
base_folder = '/home/jenner/tosync/photos-to-process'

def printMenu(f, fObj):

  print("--------------------------------------------")
  print(f"--- {f}")
  print("--- albuminfo ------------------------------")
  for key in fObj.keys():
    if key in mainKeys:
        if "\n" in fObj[key]:
            print(f"[{key[0]}] {key}: {fObj[key]}", end="")
        else:
            print(f"[{key[0]}] {key}: {fObj[key]}", end="\n")
    else: 
        if "\n" in fObj[key]:
            print(f"    {key}: {fObj[key]}", end="")
        else:
            print(f"    {key}: {fObj[key]}", end="\n")
  print("[o] open the file for hand-editing")
  print("[x] everything looks good")
  print("--------------------------------------------\n")

  fObj["title"] = "FOOOOO"


## main

print("interactiveAlbuminfo.py")

# get in the right dir
if not os.path.isdir(base_folder):
  print(f"{base_folder} does not exist.\nexiting...")
  input("Press [Enter] to continue.")
  exit()
else:
  os.chdir(base_folder)

# get the list of folders
foldersList = glob.glob("*", recursive=False)

# inspect and get user input for each folder
for f in foldersList:

    albuminfo_path = f"{f}/albuminfo"
    fObj = {}

    # use the minimum fields fields in mainKeys
    # but we will preserve any other fields
    # that already exist in the file
    for key in mainKeys:
      fObj[key] = ""

    # update fObj with albuminfo file data
    if os.path.isfile(albuminfo_path):
        with open(albuminfo_path) as albuminfoFile:
            for line in albuminfoFile:
                line = line.split(": ")
                fObj[line[0]] = line[1]

    # update fObj with user input
    printMenu(f, fObj)

#    # write out the updated fObj to albuminfo
#    with open(albuminfo_path, "w") as albuminfoFile:
#      for key in fObj:
#        f.write(f"{key}: {fObj[key]}\n")

    del fObj
    
