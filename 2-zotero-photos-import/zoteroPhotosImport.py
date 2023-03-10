# zoterOPhotosImport.py

import os, glob, re
from datetime import datetime

base_folder = "/home/jenner/tosync/photos-to-process"
dest_folder = "/home/jenner/files"
obsi_folder = "/home/jenner/obsidian"
temp_folder = "/home/jenner/tosync"

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def parseCitekey(strToParse):
  regex = re.compile(r'(?P<name>[a-zA-Z]+)(?P<year>[0-9]+)(?P<title>\w+)')
  res = regex.search(strToParse)
  return res

print("zoteroPhotosImport.py")

# if the folder does not exist, exit with an error
# if it does exist, change directory 
if not os.path.isdir(base_folder):
  print(f"{base_folder} does not exist.\nexiting...")
  input("Press [Enter] to continue.") 
  exit()
else: 
  os.chdir(base_folder)

# glob the folders in base_folder
foldersList = glob.glob('*', recursive=True)
markdown_file = []
bibfile_entries = []
mdPrevStr = ''
mdNextStr = ''
mdTitleStr = ''

# uncomment to sort with a filter
# or sort just by filename
#foldersList.sort(key = lambda x: x.split('2006')[1])
foldersList.sort()

# for every folder in the base_folder,
# first change to that folder
for fIdx, f in enumerate(foldersList):
  mdPrevStr = ''
  mdNextStr = ''
  mdTitleStr = ''

  if f == 'albuminfo':
    continue

  os.chdir(base_folder+'/'+f)
  
  # if albuminfo doesn't exist, assign the title 'Daily'
  if not os.path.exists('albuminfo'):
    print(f, "albuminfo doesn't exist")
    mdTitleStr = 'Daily'

  # if albuminfo exists, assign any vars that have data
  else:
    with open('albuminfo') as albumInfoFile:
      for line in albumInfoFile:
        if 'prev: ' in line:
            mdPrevStr = line.lstrip('prev: ').rstrip('\n')
        if 'next: ' in line:
            mdNextStr = line.lstrip('next: ').rstrip('\n')
        if 'title: ' in line:
            mdTitleStr = line.lstrip('title: ').rstrip('\n')

  # assign any unassigned vars
  if not mdTitleStr:
    mdTitleStr = 'Daily'

  if not mdPrevStr:
    if fIdx > 0:
      mdPrevStr = parseCitekey(foldersList[fIdx-1])['year']
      mdPrevStr = datetime.strptime(mdPrevStr, '%Y%m%d')
      mdPrevStr = f"{mdPrevStr.strftime('%Y-%m-%d')}"
    else:
      mdPrevStr = "0000-00-00"

  if not mdNextStr:
    if fIdx < (len(foldersList)-1):
      mdNextStr = parseCitekey(foldersList[fIdx+1])['year']
      mdNextStr = datetime.strptime(mdNextStr, '%Y%m%d')
      mdNextStr = f"{mdNextStr.strftime('%Y-%m-%d')}"
    else:
      mdNextStr = "0000-00-00"

  # build the md file's date string from the filename
  parsedDate = parseCitekey(f)['year']
  parsedDate = datetime.strptime(parsedDate, '%Y%m%d')
  mdFileDate = parsedDate.strftime('%Y-%m-%d')
  mdFileYear = parsedDate.strftime('%Y')

  # get the markdown file full path so you can create it
  mdFilePath = f"{obsi_folder}/notes/Journal/{mdFileYear}/{mdFileDate}.md"

  # get the markdown file title
  # assign the abbreviated var for readabiity
  pD = parsedDate
  mdFileTitle = f"# {weekdays[pD.weekday()]} {pD.day} {months[pD.month-1]} {pD.year}"

  # build the markdown file nav string
  mdFileNav = f"[[{mdPrevStr}]] ??? [[Journal]] ??? [[{mdNextStr}]]"

  # rename all files in the folder
  # glob and sort the files in alphanumeric order
  filesToProcess = glob.glob('*')
  filesToProcess.sort()
  count = 1
  for fTP in filesToProcess:
    if fTP == 'albuminfo':
      continue
    
    fTPname, fTPext = os.path.splitext(fTP)

    newFileName = f"{f}{count:03}{fTPext}"
    os.system(f"mv {fTP} {newFileName}")
    count = count + 1

  print(mdFilePath)

  # keep the markdown file open while handling 
  # all the photo-related operations
  with open(mdFilePath, 'w') as mdFile:

    # add header to the markdown file
    mdFile.write(mdFileNav)
    mdFile.write("\n\n")
    mdFile.write(mdFileTitle)
    mdFile.write("\n\n")

    # glob and sort the files in number order
    photosToProcess = glob.glob('*')
    photosToProcess.sort()

    # process each photo, skipping 'albuminfo'
    for p in photosToProcess:
      if p == 'albuminfo':
        continue

      pFileName, pFileExtension = os.path.splitext(p)

      # append the photo to the markdown file
      strToPrint = f"![[{p}|sm]] "
      mdFile.write(strToPrint)

      # copy the file to the dest_folder
      strToPrint = f"cp {base_folder}/{f}/{p} {dest_folder}/photos"
      os.system(strToPrint)

      # create the bibfile entry
      text = "@graphic{"+f"{pFileName}"+",\n"
      text = text + "  title = {"+f"{mdTitleStr} #{pFileName[-3:].lstrip('0')}"+"},\n"
      if 'hanni' in pFileName:
        text = text + "  author = {Hanni, Jenner},\n"
      elif 'minarik' in pFileName:
        text = text + "  author = {Minarik, SSgt},\n"
      text = text + "  date = {" + f"{mdFileDate}" + "}\n"
      text = text + "  langid = {en},\n"
      text = text + "  file = {" + f"{dest_folder}/photos/{p}" + "}\n}\n\n"
      bibfile_entries.append(text)

    # add footer to the markdown file
    mdFile.write("\n\n")
    mdFile.write(mdFileNav)
    mdFile.write("\n\n")

  # be extra super duper sure these vars are reset
  mdPrevStr = ''
  mdNextStr = ''
  mdTitleStr = ''
  markdown_file = None
  markdown_file = []

# write out the cumulative bibfile
with open(temp_folder+'/zotero-import.bib', 'w') as f:
  for b in bibfile_entries:
    f.write(b)

