import os
import shutil
from PIL import Image

# Function to extract the year and month from the image metadata
def get_image_date(image_path):
    try:
        with Image.open(image_path) as img:
            info = img._getexif()
            if info is not None:
                for tag, value in info.items():
                    if tag == 36867:  # Tag for 'DateTimeOriginal'
                        year = value[:4]
                        month = value[5:7]
                        return year, month
    except (AttributeError, OSError, IndexError):
        pass
    return None, None

# Source and destination directories
source_directory = "/home/alohawot/Desktop/2020/202001_a"
destination_directory = "/home/alohawot/Desktop/sorted"

# Create destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Variables to track statistics
num_sorted = 0
num_not_sorted = 0
formats_not_sorted = set()

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    # Check if the file is an image
    if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png")):
        # Get the year and month when the image was taken
        year, month = get_image_date(file_path)

        if year is not None and month is not None:
            # Create a directory for the year if it doesn't exist
            year_directory = os.path.join(destination_directory, year)
            if not os.path.exists(year_directory):
                os.makedirs(year_directory)

            # Create a directory for the month if it doesn't exist
            month_directory = os.path.join(year_directory, month)
            if not os.path.exists(month_directory):
                os.makedirs(month_directory)

            # Move the image to the appropriate directory
            destination_path = os.path.join(month_directory, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {month_directory}")
            num_sorted += 1
        else:
            print(f"Could not determine the year for {filename}")
            num_not_sorted += 1
            file_format = os.path.splitext(filename)[1]
            formats_not_sorted.add(file_format)

print("Sorting completed.")
print(f"Files sorted: {num_sorted}")
print(f"Files not sorted: {num_not_sorted}")
print("Formats of files not sorted:", ", ".join(formats_not_sorted))