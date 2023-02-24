# Zotero photo batch import

I use Obsidian and Zotero for my image management. This script allows the automatic import of individual files as well as folders of photo collections. 

## Procedure

### Preparation

1. Move individual files into the `~/tosync/photos-to-process` base folder.
1. Rename individual files to 'nameYYYYMMDDthreewordtitle' format where the MMDD are optional. 
1. For photo albums, manually create a folder following that naming scheme and move filenames into it in album order. 

### Script

1. Run the script from any folder, it will `cd ~/tosync/photos-to-process`. 
1. The script identifies and creates Zotero RDF entries for individual files in the base folder.
1. The script renames every file in a folder to the name of that folder with a three-digit integer, i.e. `nameYYYYMMDDthreewordtitle001`.
1. Manually batch import folders of existing photos image files by creating a Zotero RDF import to preserve the 
attachment links. [link](2-zotero-photos-import)

given a base folder,

