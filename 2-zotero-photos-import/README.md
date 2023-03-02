# Zotero Photo Batch Import

I use Obsidian and Zotero for my image management. This script allows the automatic import of individual files as well as folders of photo collections. 

## Usage

I should be able to run it from the terminal with the alias `zot` without having to navigate to any directories.

All folders and files to process should be in `~/tosync/photos-to-process`.

Each folder should be named in the form `mynameYEARMMDDalbumtitle`.

The name of the contained files doesn't matter at all. They'll be processed in alphanumerical order. 

## Procedure

### Preparation

1. For collections of photos, manually create a folder following the naming scheme and move filenames into it in album order. 
1. In each folder, include an `albuminfo` file for previous and next links, and a title for Zotero's artwork item title:

```
prev: 2004-01-09
next: 2004-01-12
title: Zotero Photo Item  Title
```

### Script

1. Run the script from any folder, it will use the default folder `~/tosync/photos-to-process`. 
1. The script identifies and creates Zotero .bibfile entries for individual files in the base folder.
1. The script renames every file in a folder to the name of that folder with a three-digit integer, i.e. `nameYYYYMMDDthreewordtitle001` in alphanumerical order.
1. The script creates a markdown file of the form `YYYY-MM-DD` for use in Obsidian. If albuminfo or one of the params in albuminfo is missing, the script autofills with the previous day and next day based on the current entry's day. 
1. The script copies the photo files into `~/files/photos`.

### Manual Zotero Import

1. Manually batch import folders of existing photos image files by uploading the Zotero .bibfile.
1. The type needs to be set to Artwork manually. Copy the object string below to the clipboard and select all of the items. Right click and select `Paste item type`. 
1. When the items are all showing up as Artwork, right click again and select `Paste into empty item fields`.

```
{
  "itemType": "artwork",
  "language": "en",
  "medium": "Photograph"
}
```

