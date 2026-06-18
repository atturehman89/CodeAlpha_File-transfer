README
Move JPG Files from One Folder to Another
Aim

This program is used to move all .jpg and .jpeg image files from a source folder to a destination folder automatically.

Description

The program checks a source folder and finds all image files with .jpg or .jpeg extension. It then moves those files into another folder. 
If the destination folder does not exist, the program creates it. If a file with the same name already exists in the destination folder, 
the program renames the new file to avoid overwriting.

Modules Used
os – Used for folder and file operations.
shutil – Used for moving files from one location to another.


Folder Structure

project_folder/

│

├── source_images/

│   ├── image1.jpg

│   ├── image2.jpeg

│   └── sample.png

│

├── jpg_files/

│

└── move_jpg_files.py

How the Program Works

Checks whether the source folder exists.
Creates the source folder if it is not present.
Creates the destination folder if it does not exist.
Scans all files in the source folder.
Identifies files ending with .jpg or .jpeg.
Moves the files to the destination folder.
Avoids overwriting by adding numbers to duplicate filenames.
Displays the number of files moved and skipped.

Sample Output

Created destination folder: 'jpg_files'

Moved: photo1.jpg -> jpg_files/photo1.jpg

Moved: photo2.jpeg -> jpg_files/photo2.jpeg

--- Summary ---

Files moved: 2

Files skipped/failed: 0

Features

Supports both .jpg and .jpeg files.

Creates required folders automatically.

Prevents accidental file overwriting.

Shows a summary after execution.

Simple and easy to understand program.

Conclusion

This program successfully moves all JPG image files from one folder to another folder.
It also handles duplicate filenames and missing folders, making the program more reliable and user friendly.
The code is simple and can be modified easily for other file types also.
