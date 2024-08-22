import os
import sys
import zipfile
import PySimpleGUIWx as sg  # Use the wxPython version of PySimpleGUI
import shutil

# Define image and video file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', '.webm', '.m4v']

# Create a simple GUI to select the ZIP file
sg.theme('DarkAmber')
layout = [
    [sg.Text('Select a ZIP file to clean')],
    [sg.Input(), sg.FileBrowse(file_types=(("ZIP files", "*.zip"),))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Delete Media From ZIP', layout)
event, values = window.read()
window.close()

if event == 'Cancel' or not values[0]:
    print("No file selected. Exiting.")
    sys.exit()

zip_file_path = values[0]

# Create a temporary folder to extract ZIP contents
temp_folder = os.path.join(os.getcwd(), "temp_zip_extraction")
os.makedirs(temp_folder, exist_ok=True)

# Extract the selected ZIP file to the temporary folder
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_folder)

# Delete image and video files within the extracted contents
for root, dirs, files in os.walk(temp_folder):
    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions + video_extensions):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# Create a new ZIP file without the deleted files
output_zip_file_path = os.path.splitext(zip_file_path)[0] + "_cleaned.zip"
with zipfile.ZipFile(output_zip_file_path, 'w') as zip_ref:
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            file_path = os.path.join(root, file)
            zip_ref.write(file_path, os.path.relpath(file_path, temp_folder))

# Clean up the temporary folder
try:
    shutil.rmtree(temp_folder)  # Safely remove the entire directory tree
    print(f"Temporary folder '{temp_folder}' has been removed.")
except Exception as e:
    print(f"Error removing temporary folder '{temp_folder}': {e}")

sg.popup('Success', f'Cleaned ZIP file created: {output_zip_file_path}')
