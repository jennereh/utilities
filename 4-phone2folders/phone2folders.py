# phone2folders.py
# handles .HEIC, .PNG, .JPG, and .GIF 
# with or without 
# ---
# missing exif data goes to 'manual

import os, glob, imghdr
from PIL import Image, UnidentifiedImageError

def get_date_taken(path):

  try:
    exif = Image.open(path)._getexif()
  except AttributeError as e:
    return 'FAIL'
  except UnidentifiedImageError as e:
    return 'FAIL'
  except FileNotFoundError as e:
    return 'FAIL'
  else:
    if not exif:
      return 'FAIL'
    elif 36867 in exif:
      return exif[36867]
    else:
      return 'FAIL'

fixme_folder = "manualfix"
desk_folder = "/home/jenner"
dest_folder = "/home/jenner/tosync/photos-to-process"
file_prefix = "iPhone_c"
albuminfo   = "title: Daily"

print("phone2folders.py")

# if the folders do not exist, exit with an error
# if they do exist, change to the desktop
if not os.path.isdir(dest_folder):
  print(f"{dest_folder} does not exist.\nexiting...")
  input("Press [Enter] to continue.") 
  exit()
else: 
  os.chdir(desk_folder)

# glob the folders in base_folder
filesList = glob.glob(f"{file_prefix}*", recursive=False)

for f in filesList:

  newFileName = ''
  fName, fExt = os.path.splitext(f)

  # process files by type
  # - create JPG from HEIC and put original HEIC in trash
  # - some iPhone screenshots that have been edited appear to 
  #   have a suffix of .png but are actually .jpg files (what?!)
  #   so detect and convert these 
  # - all other image files with dates get lowercase exts
  if fExt == '.HEIC':    
    newFileName = f"{fName}.jpg"
    os.system(f"heif-convert {f} {newFileName}")
    os.system(f"gio trash {f}")
  elif fExt == '.PNG' or fExt == '.png':
    if imghdr.what(f) == 'jpeg':
      newFileName = f"{fName}.jpg"
      os.system(f"mv {f} {newFileName}")
    else:
      newFileName = f"{fName}{fExt.lower()}"
      os.system(f"mv {f} {newFileName}")
  else:  
    newFileName = f"{fName}{fExt.lower()}"
    os.system(f"mv {f} {newFileName}")

  print(f"{newFileName} is ready to be moved")

  # now figure out where to put the file
  # build the destination folder's name from the exif data
  date = get_date_taken(newFileName)
  if date == 'FAIL':
    newFolderPath = dest_folder+'/'+fixme_folder
  else:
    date = date.split(' ')[0].split(':')
    yr = date[0]
    mo = date[1]
    dy = date[2]
    newFolderName = f"hanni{yr}{mo}{dy}daily"
    newFolderPath = dest_folder+'/'+newFolderName

  # make sure the destination folder exists
  if not os.path.isdir(newFolderPath):
    os.system(f"mkdir {newFolderPath}")

  # create an albuminfo file if necessary
  if not os.path.isfile(f"{newFolderPath}/albuminfo"):
    with open(newFolderPath+'/albuminfo', 'w') as albuminfoFile:
      albuminfoFile.write(albuminfo)

  # move the file to its dated destination folder
  os.system(f"mv {newFileName} {newFolderPath}/{newFileName}")


