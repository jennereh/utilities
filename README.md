# utilities
Data mangling, mostly. 

1. parseCitekey parses Zotero citekeys. [link](https://github.com/jennereh/utilities/blob/main/1-parsecitekey/parseCiteKey.py)

2. zoteroPhosoImport manually batch imports folders containing photo files by renaming files to match the folder, reading related information from a text file in the folder, manually creating a Zotero RDF file that preserves attachment links, and creating a markdown file for any photo albums for use for use in Obsidian. [link](2-zotero-photos-import)

3. zoteroReconcile is a one-off script to reconcile a folder of misplaced files against the existing Zotero .bib BibLaTex file that lost them. [link](https://github.com/jennereh/utilities/blob/main/3-zotero-reconcile/zoteroReconcile.py)

4. phone2folders processes iPhone photos and screenshots that have been moved to my laptop with Feem, converting the images from HEIC to JPG and sorting them into folders by date. [link](4-phone2folders)

5. interactiveAlbuminfo iterates through a set of daily folders, prompting for a title and dates for the albuminfo file. This should make editing daily random photo entries easy enough to actually do it. [link](5-interactive-albuminfo)

6. insertJournalPage inserts a page in the Journal section with nothing more than the date. [link](6-insert-journal-page)
