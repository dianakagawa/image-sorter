This Python script allows the user to organize and sort images based on their capture date into separate folders by year and month. Please note that the script relies on image metadata to determine the capture date. In some cases, image metadata may be missing or not in the expected format, which could result in inaccurate sorting or files being skipped.

## Features

- Sorts images by their capture date into year and month folders.
- Supports popular image formats: JPEG (.jpg, .jpeg) and PNG (.png).
- Provides statistics on the number of files sorted and files that couldn't be sorted.
- Displays the formats of the files that couldn't be sorted.

## Getting Started

### Prerequisites

- Python 3.7 or above
- Pillow library (install using `pip install pillow`)

### Usage

1. Clone the repository or download the script file (`app.py`) to your local machine.

2. Open the script file (`app.py`) in a text editor.

3. Update the source and destination directory paths in the script:

   - Set `source_directory` to the path of the directory containing the folders with images to be sorted.
   - Set `destination_directory` to the path of the directory where you want to organize the images.

4. Save the changes made to the script.

5. Open a terminal or command prompt and navigate to the directory where the script is located.

6. Run the script using the following command:

   ```bash
   python app.py
   ```
