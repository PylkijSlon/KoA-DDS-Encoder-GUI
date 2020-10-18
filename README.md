# KoA-DDS-Encoder

1) Unpack the gui.exe and gui.css into the same folder directory as the KOARR_dds_encoder.exe (the gui.exe is currently not available on GitHub. I will update with a link to a download as soon as one is available).

2) Set the absolute file paths for the pakfilebuilder.exe, pakfileunpacker.exe and KOARR_dds_encoder.exe on the Setting tab.

## Usage

This is a very alpha version created to match the release of the KoA Encoding/Decoding tools by Szlobi and to extend GUI support to the pakfilebuilder and pakfileunpacker released by the developers. You may set the pakfilebuilder.exe, pakfileunpacker.exe, and KOARR_dds_encoder.exe paths under the settings tab.

### Unpacking
To unpackage a KoA.pak, select the KoA data directory, select a target directory and choose a .pak you wish to unpack. Any 3rd party .pak can also be unpacked this way, however, this GUI does not currently support absolute file paths for unpacking. In addition, you may specify specific file(s) that you wish to unpack: enter them into the Specific Files field, including their extension (i.e. 3240.dds), separated by a ‘,’. You create a list of all files contained within a .pak by using the ‘List’ function. The list will be created in the GUI root folder.

### Packaging
To package a KoA.pak, select a directory you wish to create a .pak of and name your .pak (omitting the file extension at the end). This does not ensure that your .pak works, only that it is built. The package will be created in the GUI root folder.

### Decoding
To decode a KoA.dds that you have unpacked, input the target directory and use the ‘Decode’ function. Single or multiple *.dds files can be decoded by entering the absolute file paths in the text box, or you can decode a directory using the ‘Decode Source Directory’ line. The text box is read only: to enter file paths, use the ‘Browse’ button to the right.

### Encoding
To re-encode a *.dds to KoA format that you have edited, input the target directory and use the ‘Encode’ function. Single or multiple. *.dds files can be re-encoded by entering the absolute file paths in the text box, or you can re-encode a directory using the ‘Encode Source Directory’ line. The text box is read only: to enter file paths, use the ‘Browse’ button to the right.

Encoding files into KoA.dds format is more complicated than simply choosing a file. Therefore, I would recommend you read the documentation provided by Szlobi for the encoder.exe and any follow up questions should be directed to the #modding channel on Discord.

## Python Modules

gui.py uses the following python modules:

### Standard
1) sys

2) os

3) subprocess

4) fnmatch

### Non-standard
5) PyQt5

All non-standard (as of python 3.8.5 on Windows) will need to be installed to run gui.py. I would recomend using pip.

## Final Notes
The stylesheet was created by Jamie A. Quiorga P. and can be found at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss

The GUI is written using PyQt5 under its GPL license. You may redistribute it freely, however it cannot be sold.

Source code for the GUI and a copy of the GNU GPL v3.0 is available on GitHub at: https://github.com/PylkijSlon/KoA-DDS-Encoder


