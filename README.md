# KoA-DDS-Encoder

1) Unpack the gui.exe and gui.css into the same folder directory as the KOARR_dds_encoder.exe

2) Set the absolute file paths for the pakfilebuilder.exe, pakfileunpacker.exe and KOARR_dds_encoder.exe on the Setting tab.

3) Follow the instructions for Unpacking, Packing, Decoding, and Encoding on the Main tab.

The stylesheet was created by Jamie A. Quiorga P. and can be found at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss

The GUI is written using PyQt5 under its GPL license. You may redistribute it freely, however it cannot be sold.

Source code for the GUI and a copy of the GNU GPL v3.0 is available on GitHub at: https://github.com/PylkijSlon/KoA-DDS-Encoder

## Python Modules

gui.py uses the following python modules:

### Standard
1)sys

2)os

3)subprocess
### Non-standard
4)fnmatch

5)PyQt5

All non-standard (as of python 3.8.5 on Windows) will need to be installed. I would recomend using pip 
