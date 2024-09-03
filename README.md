# CleanZIP


CleanZIP is a lightweight tool designed to clean ZIP files by removing all media files (e.g., images and videos) by keeping only specific file types (i.e., .csv, .html, and .json). This tool is particularly useful for anyone who needs to sanitize ZIP files from data donation packages before sharing or archiving them.

## Features

+ File Type Filtering: Automatically delete or keep only specific file types within a ZIP archive.
+ Cross-Platform Support: Works on Windows, macOS, and Linux (Ubuntu).
+ User-Friendly GUI: Easy-to-use graphical interface for selecting and processing ZIP files.




## Prerequisites

To use CleanZIP, you will just need to download the latest file from releases:

[https://github.com/favstats/CleanZIP/releases](https://github.com/favstats/CleanZIP/releases)

## Usage  

+ Select a ZIP File:

    Use the GUI to browse and select the ZIP file you want to clean.

+ Process the ZIP File:

    The tool will remove all files except those with .csv, .html, and .json extensions (as configured).

    A new cleaned ZIP file will be created in the same directory with the suffix _cleaned.zip.

+ View Results:

    A popup will inform you of the success, and you can view the cleaned ZIP file at the specified location.


### Instructions for **Windows Users**

![](https://codesigningstore.com/wp-content/uploads/2021/10/windows-protected-your-pc.svg)

When running CleanZIP on Windows, you might encounter a warning from Windows SmartScreen, which is a security feature designed to prevent unrecognized apps from running. If you see this warning, don't worry—CleanZIP is safe to use!

#### To bypass the Windows SmartScreen warning:

+ When the SmartScreen dialog appears, click on "More info".

+ Then, click on the "Run anyway" button.

+ This is normal for applications that are not widely downloaded. Since CleanZIP is an open-source tool, you can review the source code here on GitHub to confirm its safety.

## How It Was Built

CleanZIP is developed using Python and leverages the `PySimpleGUIWx` library for the graphical user interface, making it accessible to users with minimal technical expertise. The tool uses the zipfile module for ZIP file operations and `os` and `shutil` modules for file management, ensuring robust and efficient file processing.

## Trust and Credibility

CleanZIP is privacy-sensitive and respects the confidentiality of your data:

+ **Open Source**: The source code is fully open source and available on GitHub. You can inspect it yourself to ensure there are no hidden functionalities or privacy risks.
+ **Local Processing**: All processing is done locally on your machine. CleanZIP does not send any data over the internet, ensuring that your files remain private.
+ **Minimal Permissions**: The tool only requires access to the files you yourself select for processing.

CleanZIP was developed by Dr. Fabio Votta, a researcher and software developer at the University of Amsterdam. This tool was created to streamline the process of cleaning and sanitizing ZIP files, particularly in academic and research settings where data sharing and integrity are paramount.

## Contributions

Contributions to CleanZIP are welcome! If you have ideas for improvements or have found a bug, feel free to open an issue or submit a pull request.

## License

CleanZIP is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or support, please contact:

Dr. Fabio Votta
Researcher, University of Amsterdam
f.a.votta@uva.nl

