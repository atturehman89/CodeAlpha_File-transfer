"""
Task 3: Move all .jpg files from a source folder to a new folder.

Key concepts used: os, shutil, file handling
"""

import os
import shutil

# ----- Configuration: change these paths as needed -----
SOURCE_FOLDER = "source_images"
DEST_FOLDER = "jpg_files"
# ---------------------------------------------------------


def move_jpg_files(source_folder, dest_folder):
    """Move all .jpg/.jpeg files from source_folder into dest_folder."""

    # Create the source folder if it doesn't exist (so the script doesn't crash
    # on a fresh run); in real use this folder should already contain files.
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist. Creating it now.")
        os.makedirs(source_folder)
        print("Add some .jpg files there and run the script again.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: '{dest_folder}'")

    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(source_folder):
        # Case-insensitive match for .jpg and .jpeg
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)

            # Skip directories that happen to have a .jpg-like name
            if not os.path.isfile(source_path):
                continue

            # Avoid overwriting a file that already exists at the destination
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                while os.path.exists(new_dest_path):
                    counter += 1
                    new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                dest_path = new_dest_path

            try:
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename} -> {dest_path}")
                moved_count += 1
            except Exception as e:
                print(f"Failed to move {filename}: {e}")
                skipped_count += 1

    print("\n--- Summary ---")
    print(f"Files moved:  {moved_count}")
    print(f"Files skipped/failed: {skipped_count}")
    if moved_count == 0 and skipped_count == 0:
        print("No .jpg files found in the source folder.")


if __name__ == "__main__":
    move_jpg_files(SOURCE_FOLDER, DEST_FOLDER)