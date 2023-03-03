# phone2folders

Automate moving iPhone photos and screenshots to my laptop with Feem, converting any HEIC images to JPG, sorting all imported images into folders by date, and saving any extras in a manual fixes folder for later inspection. [link](4-phone2folders)

## Dependencies

I'm running Linux Mint 20.

1. Files are moved to the trash using `gio` 
1. `.HEIC` files are converted using `heif-convert`

## Prep

1. Install the Feem app on the iPhone. 
1. Feem's AppImage lives in `~/admin` on the laptop.
1. Connect the phone and the laptop to the same wifi.
1. Open the Feem app on both devices.
1. Manually click to transfer all of the files from one to the other. 
1. The transfer often doesn't actually complete, so check the size of the files on the laptop with the total displayed on the hone. If it's wrong, send them all again, Feem will only send the ones that were missed. Do this until all files have been transferred. 
1. Don't delete anything on the phone until this process is complete.

## Usage

I should be able to run this script from the terminal with the alias `phone2folders` without having to navigate to any directories. Added the following to my `.bashrc`.

```
alias phone2folders="python /home/jenner/projects/jeh-utilities/4-phone2folders/phone2folders.py"
```

All imported files to process should be in `~/` and start with `iPhone_c`.

As of March 2023, the files seem to be a combination of `.PNG`, `.GIF`, `.JPG`, and `.HEIC`.

This script moves all files to new folders in `~/tosync/photos-to-process` by date.

Each folder should be named in the form `mynameYEARMMDDdaily`.

Each folder should also contain an `albuminfo` text file with a single line `title: Daily`.

The output should be formatted so `zot` can be run immediately.

## Next Step

1. Go through each folder and hand-edit the images in the folders.
1. Update the `albuminfo` file if needed. 
1. Run the `zot` script from [2-zotero-photos-import](https://github.com/jennereh/utilities/tree/main/2-zotero-photos-import). The files in each folder will be processed in alphanumerical order.

## Finish

1. Check all of the Obsidian journal entries to be sure the photos came in as expected.
1. Delete all of the photos on the phone.
