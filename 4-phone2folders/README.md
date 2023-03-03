# phone2folders

Developing process for moving iPhone photos and screenshots to my laptop with Feem, converting the images from HEIC to JPG, sorting them into folders by date. [link](4-phone2folders)

## Prep

1. Install the Feem app on the iPhone. 
1. Feem's AppImage lives in `~/admin` on the laptop.
1. Connect the phone and the laptop to the same wifi.
1. Open the Feem app on both devices.
1. Transfer all of the files from one to the other. 
1. The transfer often doesn't actually complete, so check the size of the files on the laptop with the total displayed on the hone. If it's wrong, send them all again, Feem will only send the ones that were missed. Do this until all files have been transferred. 
1. Don't delete anything on the phone until this process is complete.

## Usage

I should be able to run the script from the terminal with the alias `phone2folders` without having to navigate to any directories.

All files to process should be in `~/` and start with `iPhone_`.

This script moves all files to new folders in `~/tosync/photos-to-process` by date.

Each folder should be named in the form `mynameYEARMMDDdaily`.

Each folder should also contain an `albuminfo` text file with a single line `title: Daily`.

## Next Step

1. Go through each folder and hand-edit the images in the folders.
1. Update the `albuminfo` file if needed. 
1. Run the `zot` script from [2-zotero-photos-import](https://github.com/jennereh/utilities/tree/main/2-zotero-photos-import). The files in each folder will be processed in alphanumerical order.

## Finish

1. Check all of the Obsidian journal entries to be sure the photos came in as expected.
1. Delete all of the photos on the phone.
