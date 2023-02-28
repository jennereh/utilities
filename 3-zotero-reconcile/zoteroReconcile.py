# This is a one-shot script to reconcile old folders.
#
# As part of my Zotero workflow, I link attachments instead of
# storing them directly in Zotero. Don't do what I do, I don't
# know why I do it, I just hate having files vanish into Zotero's
# db. But it adds a lot of hassle and stress. I have to manually
# link attachments when importing, for example.
#
# In this case I had a folder (~/files-old) full of files.
# I had an existing .bib file with tons of entries, many of which
# knew about those files as local links.
#
# This is a script to reconcile the following:
# - a folder containing files in the form 'citekey.whatever'
# - a Zotero .bib BibLaTeX export
# The script should:
# - move all files that exist into the original files folder
#   so Zotero now recognizes those linked attachments again
# Manual postprocessing required!
# - any leftover files need to be handled by hand
#   ... turns out I had a couple of illegal citekeys
#       containing ampsersands. And a few that weren't in the
#       .bibfile. Easy to fix by hand.

import os, glob, bibtexparser

source_folder = "/home/jenner/files-old"
dest_folder = "/home/jenner/files"

bibfile = "/home/jenner/obsidian/bibfile/zotero.bib"

# get list of files in source_folder
os.chdir(source_folder)
filesList = glob.glob('*')

# get list of .bib file database entries
parser = bibtexparser.bparser.BibTexParser()
parser.ignore_nonstandard_types = False
with open(bibfile) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file, parser)

# for each source file, check if it exists in the bibfile
# if it does, move it
# if not, do nothing
for f in filesList:

    for b in bib_database.entries:
        if 'file' in b:
            cmdStr = f"mv {f} {dest_folder}"
            os.system(cmdStr)
            print(cmdStr)
            break
