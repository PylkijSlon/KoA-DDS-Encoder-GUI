import sys
import os
import subprocess
import fnmatch
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

	def __init__(self):
		super().__init__()
		#Main UI Code

		#Footer Buttons
		def settings():
			tabs.setCurrentIndex(1)

		def cancel():
			self.close()

		#Action Buttons

		#Input List
		def input_list():
			if ent_dir_pak_builder.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Path to PakBuilder.exe not set.')
				return

			elif ent_dir_pak.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please choose the directory you wish to pack.')
				return

			elif ent_pak_create.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please choose a name for the pak file you wish to create.')
				return

			else:
				#Message
				msg_title = 'Creating Your Input List'
				msg_text = 'The list of files you wish to pack is being created.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()

				#List
				path = ent_dir_pak.text() + '/'
				input_list = ent_pak_create.text() + '.txt'
				dirs = os.listdir(path)
				with open(input_list, 'w', encoding='utf-8') as f:
					for item in dirs:
						f.write(path + "%s\n" % item)

		#Pack
		def create_pak():
			#Make List
			if ent_dir_pak_builder.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Path to PakBuilder.exe not set.')
				return

			elif ent_dir_pak.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please choose the directory you wish to pack.')
				return

			elif ent_pak_create.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please choose a name for the pak file you wish to create.')
				return

			else:
				#Message
				msg_title = 'Creating Your Input List'
				msg_text = 'The list of files you wish to pack is being created.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()

				#List
				path = ent_dir_pak.text() + '/'
				input_list = ent_pak_create.text() + '.txt'
				dirs = os.listdir(path)
				with open(input_list, 'w', encoding='utf-8') as f:
					for item in dirs:
						f.write(path + "%s\n" % item)

				#Build Pack
				builder = ent_dir_pak_builder.text()
				input_list = os.path.abspath(ent_pak_create.text()) + ".txt"
				pak = ent_pak_create.text() + ".pak"

				#Message
				msg_title = 'Building' + pak
				msg_text = 'Your .pak is being built. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()

				try:
					pak_builder = subprocess.Popen([builder, "-c", input_list, pak],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
				except Exception as ex:
					print(ex)
    
				else:
					print(pak_builder.communicate())

		#Unpack
		def unpack_pak():
			if ent_dir_pak_unpacker.text() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the directory of the pakfileunpacker.exe")
				return

			elif ent_dir_data.text() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the data directory where the .pak file is located.")
				return

			elif ent_pak_unpack.text() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the name of the .pak file you wish to unpack.")
				return
    
			elif ent_dir_target.text() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the directory you wish to unpack into.")
				return

			elif ent_unpack_files.toPlainText() == '':
				unpacker = ent_dir_pak_unpacker.text()
				path = ent_dir_data.text() + "/"
				pak = ent_pak_unpack.text() + ".pak"
				target = ent_dir_target.text() + "/"

				#Message
				msg_title = 'Unpacking' + pak
				msg_text = 'Your .pak is being unpacked. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()

				try:
					unpacker_unpack = subprocess.Popen([unpacker, path + pak, 'unpack', target],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
					print(ent_unpack_files.toPlainText())
					
				except Exception as ex:
					print(ex)
    
				else:
					print(unpacker_unpack.communicate())

			else:
				unpacker = ent_dir_pak_unpacker.text()
				path = ent_dir_data.text() + "/"
				pak = ent_pak_unpack.text() + ".pak"
				target = ent_dir_target.text() + "/"
				files = ent_unpack_files.toPlainText()

				files_lst = []
				for subs in files.split(','):
					files_lst.append(subs)

				for item in files_lst:
					print(item.strip())

				for item in files_lst:
					unpacker_unpack = subprocess.Popen([unpacker, path + pak, 'unpack', target, item.strip()],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
					print(unpacker_unpack.communicate())

		#List
		def list_pak():		
			if ent_dir_pak_unpacker.text() == "":
				qtw.QMessageBox.information(self, "Error", "Please set the directory of the pakfileunpacker.exe")
				return

			elif ent_dir_data.text() == "":
				qtw.QMessageBox.information(self, "Error", 'Please set the data directory where the .pak file is located.')
				return

			elif ent_pak_unpack.text() == "":
				qtw.QMessageBox.information(self, "Error", "Please set the name of the .pak file you wish to list the contents of.")
				return

			else:
				unpacker = ent_dir_pak_unpacker.text()
				path = ent_dir_data.text() + "/"
				pak = ent_pak_unpack.text() + ".pak"
				pak_list_file = ent_pak_unpack.text() + ".txt"

				#Message
				msg_title = 'Listing Files'
				msg_text = 'Creating a list of files in:' + pak + '. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()

				try:
					unpacker_list = subprocess.Popen([unpacker, path + pak, 'list'],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
				except Exception as ex:
					print(ex)

				else:
					pak_contents = unpacker_list.stdout.read()

					print(unpacker_list.communicate())
					
					with open(pak_list_file, 'w', encoding='utf-8') as f:
						f.write(pak_contents)

		def encode_function():
			if ent_path_encoded.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please set the target directory')

			elif ent_path_encode.toPlainText() == '':
				msg_title = 'Encoding Directory'
				msg_text = 'Encoding your .dds Files from Standard Format to KoA Format. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()
				encode_dir()

			else:
				msg_title = 'Encoding Files'
				msg_text = 'Encoding your .dds Files from Standard Format to KoA Format. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()
				encode_files()

		def encode_files():
			encoder = ent_dir_encoder.text()
			filepath = ent_path_encode.toPlainText()
			target = ent_path_encoded.text()

			dds_names = []
			for subs in filepath.split(','):
				dds_names.append(subs)

			with open('targetPath.txt', 'w') as f:
				f.write(target)

			for item in dds_names:
				print(item.strip())
				encode = subprocess.Popen([encoder, '2', item.strip()],
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				print(encode.communicate())
				encode.terminate()

		def encode_dir():
			encoder = ent_dir_encoder.text()
			directory = ent_dir_encode.text()
			target = ent_path_encoded.text()

			dir_lst = fnmatch.filter(os.listdir(directory), '*.dds')

			absolute_lst = []
			for i in dir_lst:
				absolute = directory + '/' + i
				absolute_lst.append(absolute)

			with open('targetPath.txt', 'w') as f:
				f.write(target)

			for item in absolute_lst:
				encode = subprocess.Popen([encoder, '2', item],
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				print(encode.communicate())
				encode.terminate()

		def decode_function():
			if ent_path_decoded.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please set the target directory')

			elif ent_path_decode.toPlainText() == '':
				msg_title = 'Decoding Directory'
				msg_text = 'Decoding your .dds Files from KoA Format to Standard. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()
				decode_dir()

			else:
				msg_title = 'Decoding Files'
				msg_text = 'Decoding your .dds Files from KoA Format to Standard. Please be patient.'
				msg_box.setText(msg_title)
				msg_box.setInformativeText(msg_text)
				msg_box.exec_()
				decode_files()

		def decode_files():
			encoder = ent_dir_encoder.text()
			filepath = ent_path_decode.toPlainText()
			target = ent_path_decoded.text()

			dds_names = []
			for subs in filepath.split(','):
				dds_names.append(subs)

			with open('targetPath.txt', 'w') as f:
				f.write(target)

			for item in dds_names:
				decode = subprocess.Popen([encoder, '1', item.strip()],
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				print(decode.communicate())
				decode.terminate()

		def decode_dir():
			encoder = ent_dir_encoder.text()
			directory = ent_dir_decode.text()
			target = ent_path_decoded.text()

			dir_lst = fnmatch.filter(os.listdir(directory), '*.dds')

			absolute_lst = []
			for i in dir_lst:
				absolute = directory + '/' + i
				absolute_lst.append(absolute)

			with open('targetPath.txt', 'w') as f:
				f.write(target)

			for item in absolute_lst:
				decode = subprocess.Popen([encoder, '1', item],
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				print(decode.communicate())
				decode.terminate()

		#Browse Buttons

		#Settings
		def browse_pak_builder():
			filepath = qtw.QFileDialog.getOpenFileName()[0]
			ent_dir_pak_builder.clear()
			ent_dir_pak_builder.setText(filepath)
			with open('pakfilebuilder_path.txt', 'w') as f:
				f.write(filepath)

		def browse_pak_unpacker():
			filepath = qtw.QFileDialog.getOpenFileName()[0]
			ent_dir_pak_unpacker.clear()
			ent_dir_pak_unpacker.setText(filepath)
			with open ('pakfileunpacker_path.txt', 'w') as f:
				f.write(filepath)

		def browse_encoder():
			filepath = qtw.QFileDialog.getOpenFileName()[0]
			ent_dir_encoder.clear()
			ent_dir_encoder.setText(filepath)
			with open ('ddsencoder_path.txt', 'w') as f:
				f.write(filepath)

		#Pack/Unpack
		def browse_dir_pak():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_dir_pak.clear()
			ent_dir_pak.setText(directory)

		def browse_dir_data():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_dir_data.clear()
			ent_dir_data.setText(directory)

		def browse_dir_target():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_dir_target.clear()
			ent_dir_target.setText(directory)

		#Encode/Decode
		def browse_decode_files():
			filepath_tupple = qtw.QFileDialog.getOpenFileNames()
			filepath_list = list(filepath_tupple)
			del filepath_list[-1]
			filepath = ", ".join(filepath_list[0])
			ent_path_decode.clear()
			ent_path_decode.setText(filepath)

		def browse_encode_files():
			filepath_tupple = qtw.QFileDialog.getOpenFileNames()
			filepath_list = list(filepath_tupple)
			del filepath_list[-1]
			filepath = ", ".join(filepath_list[0])
			ent_path_encode.clear()
			ent_path_encode.setText(filepath)

		def decoded_destination():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_path_decoded.clear()
			ent_path_decoded.setText(directory)

		def encoded_destination():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_path_encoded.clear()
			ent_path_encoded.setText(directory)

		def encode_source():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_dir_encode.clear()
			ent_dir_encode.setText(directory)

		def decode_source():
			directory = qtw.QFileDialog.getExistingDirectory()
			ent_dir_decode.clear()
			ent_dir_decode.setText(directory)

		#Layout
		layout = qtw.QVBoxLayout()
		self.setLayout(layout)
		self.setWindowTitle('GUI - KoARR DDS Encoder, Unpacker and Packer')
		self.setMinimumSize(500, 300)

		#Containers for Tabs
		tab_main = qtw.QWidget(self)
		tab_settings = qtw.QWidget(self)
		tab_pack_unpack = qtw.QWidget(self)
		tab_encode_decode = qtw.QWidget(self)
		
		layout_main = qtw.QVBoxLayout()
		tab_main.setLayout(layout_main)
		layout_pack_unpack = qtw.QVBoxLayout()
		tab_pack_unpack.setLayout(layout_pack_unpack)

		layout_encode_decode = qtw.QVBoxLayout()
		tab_encode_decode.setLayout(layout_encode_decode)

		layout_settings = qtw.QGridLayout()
		layout_settings.setColumnMinimumWidth(0, 100)
		tab_settings.setLayout(layout_settings)

		#Tabs
		tabs = qtw.QTabWidget()
		layout.addWidget(tabs)
		tabs.addTab(tab_main, 'Main')
		tabs.addTab(tab_settings, 'Settings')
		tabs.addTab(tab_pack_unpack, 'Pack/Unpack')
		tabs.addTab(tab_encode_decode, 'Encode/Decode')


		#Footer
		frm_footer = qtw.QFrame()
		layout_footer = qtw.QHBoxLayout()
		frm_footer.setLayout(layout_footer)
		btn_settings = qtw.QPushButton('Settings')
		btn_cancel = qtw.QPushButton('Cancel')
		btn_settings.clicked.connect(settings)
		btn_cancel.clicked.connect(cancel)

		layout_footer.addWidget(btn_settings)
		layout_footer.addWidget(btn_cancel)
		layout.addWidget(frm_footer)

		#Main
		lbl_main_intro = qtw.QLabel("This is a very alpha version created to match the release of the KoA Encoding/Decoding tools by Szlobi and to extend GUI support to the pakfilebuilder and pakfileunpacker released by the developers. You may set the pakfilebuilder, pakfileunpacker, and KOARR_dds_encoder paths under the settings tab. This GUI must be placed in the same folder as the KOARR_dds_encoder in order to encode and decode *.dss files.", 
			self
		)
		lbl_main_intro.setWordWrap(1)
		lbl_main_packaging = qtw.QLabel("Unpacking: To unpackage a KoA.pak, select the KoA data directory, select a target directory and choose a .pak you wish to unpack. Any 3rd party .pak can also be unpacked this way, however, this GUI does not currently support absolute file paths for unpacking. In addition, you may specify specific file(s) that you wish to unpack: enter them into the Specific Files field, including their extension (i.e. 3240.dds), seperated by a ','. You create a list of all files contained within a .pak by using the ‘List’ function. The list will be created in the GUI root folder.", 
			self
		)
		lbl_main_packaging.setWordWrap(1)
		lbl_main_unpacking = qtw.QLabel("Packaging: To package a KoA.pak, select a directory you wish to create a .pak of and name your .pak (omitting the file extension at the end). This does not ensure that your .pak works, only that it is built. The package will be created in the GUI root folder.", 
			self
		)
		lbl_main_unpacking.setWordWrap(1)
		lbl_main_encoding = qtw.QLabel("Decoding: To decode a KoA.dds that you have unpacked, input the target directory and use the ‘Decode’ function. Single or multiple *.dds files can be decoded by entering the absolute file paths in the text box, or you can decode a directory using the ‘Decode Source Directory’ line. The text box is read only: to enter file paths, use the ‘Browse’ button to the right.", 
			self
		)
		lbl_main_encoding.setWordWrap(1)
		lbl_main_decoding = qtw.QLabel("Encoding: to re-encode a *.dds to KoA format that you have edited, input the target directory and use the ‘Encode’ function. Single or multiple. *.dds files can be re-encoded by entering the absolute file paths in the text box, or you can re-encode a directory using the ‘Encode Source Directory’ line. The text box is read only: to enter file paths, use the ‘Browse’ button to the right.",
			self
		)
		lbl_main_decoding.setWordWrap(1)
		lbl_main_thoughts = qtw.QLabel("Encoding files into KoA.dds format is more complicated than simply choosing a file. Therefore, I would recommend you read the documentation provided by Szlobi for the encoder.exe and any follow up questions should be directed to the #modding channel on Discord.",
			self
		)
		lbl_main_thoughts.setWordWrap(1)

		layout_main.addWidget(lbl_main_intro)
		layout_main.addWidget(lbl_main_packaging)
		layout_main.addWidget(lbl_main_unpacking)
		layout_main.addWidget(lbl_main_encoding)
		layout_main.addWidget(lbl_main_decoding)
		layout_main.addWidget(lbl_main_thoughts)

		#Pack & Unpack
		frm_pack = qtw.QFrame(self)
		layout_pack_unpack.addWidget(frm_pack)
		frm_unpack = qtw.QFrame(self)
		layout_pack_unpack.addWidget(frm_unpack)

		#Pack Contents
		lbl_dir_pak = qtw.QLabel('Directory to Pack', self)
		lbl_pak_create = qtw.QLabel('.pak Name', self)

		ent_dir_pak = qtw.QLineEdit(self)
		ent_pak_create = qtw.QLineEdit(self)

		btn_browse_dir_pak = qtw.QPushButton('Browse', self)
		btn_browse_dir_pak.clicked.connect(browse_dir_pak)
		
		frm_pack_footer = qtw.QFrame()
		btn_create_pak = qtw.QPushButton('Pack', self)
		btn_create_pak.clicked.connect(create_pak)

		#Pack Layout
		layout_pack = qtw.QGridLayout()
		layout_pack.setColumnMinimumWidth(0, 100)
		frm_pack.setLayout(layout_pack)

		layout_pack.addWidget(lbl_dir_pak, 0, 0)
		layout_pack.addWidget(lbl_pak_create, 1, 0)

		layout_pack.addWidget(ent_dir_pak, 0, 1)
		layout_pack.addWidget(ent_pak_create, 1, 1)

		layout_pack.addWidget(btn_browse_dir_pak, 0, 2)
		layout_pack.addWidget(btn_create_pak, 2, 0)

		#Unpack Contents
		lbl_dir_data = qtw.QLabel('Data Directory', self)
		lbl_dir_target = qtw.QLabel('Target Directory', self)
		lbl_pak_unpack = qtw.QLabel('.pak Name', self)
		lbl_unpack_files = qtw.QLabel('Specific File(s)', self)

		ent_dir_data = qtw.QLineEdit(self)
		ent_dir_target = qtw.QLineEdit(self)
		ent_pak_unpack = qtw.QLineEdit(self)
		ent_unpack_files = qtw.QTextEdit(self)

		btn_browse_dir_data = qtw.QPushButton('Browse', self)
		btn_browse_dir_target = qtw.QPushButton('Browse', self)
		btn_browse_dir_data.clicked.connect(browse_dir_data)
		btn_browse_dir_target.clicked.connect(browse_dir_target)

		frm_unpack_footer = qtw.QFrame()
		btn_unpack_pak = qtw.QPushButton('Unpack', self)
		btn_unpack_list = qtw.QPushButton('List', self)

		btn_unpack_pak.clicked.connect(unpack_pak)
		btn_unpack_list.clicked.connect(list_pak)

		#Unpack Layout
		layout_unpack = qtw.QGridLayout()
		layout_unpack.setColumnMinimumWidth(0, 100)
		frm_unpack.setLayout(layout_unpack)

		layout_unpack.addWidget(lbl_dir_data, 0, 0)
		layout_unpack.addWidget(lbl_dir_target, 1, 0)
		layout_unpack.addWidget(lbl_pak_unpack, 2, 0)
		layout_unpack.addWidget(lbl_unpack_files, 3, 0)

		layout_unpack.addWidget(ent_dir_data, 0, 1)
		layout_unpack.addWidget(ent_dir_target, 1, 1)
		layout_unpack.addWidget(ent_pak_unpack, 2, 1)
		layout_unpack.addWidget(ent_unpack_files, 3, 1)

		layout_unpack.addWidget(btn_browse_dir_data, 0, 2)
		layout_unpack.addWidget(btn_browse_dir_target, 1, 2)

		layout_unpack_footer = qtw.QHBoxLayout()
		frm_unpack_footer.setLayout(layout_unpack_footer)
		layout_unpack_footer.addWidget(btn_create_pak)
		layout_unpack_footer.addWidget(btn_unpack_pak)
		layout_unpack_footer.addWidget(btn_unpack_list)
		layout_pack_unpack.addWidget(frm_unpack_footer)

		#Encode & Decode
		frm_encode_decode = qtw.QFrame()

		lbl_dir_encode = qtw.QLabel('Encode Source Directroy')
		lbl_path_encoded = qtw.QLabel('Encode Target Directory')
		#lbl_path_encoded.setWordWrap(1)
		lbl_path_encode = qtw.QLabel('Path of File(s) to Encode')
		lbl_dir_decode = qtw.QLabel('Decode Source Directory')
		lbl_path_decoded = qtw.QLabel('Decode Target Directory')
		#lbl_path_decoded.setWordWrap(1)
		lbl_path_decode = qtw.QLabel('Path of File(s) to Decode')

		ent_dir_encode = qtw.QLineEdit(self)
		ent_path_encoded = qtw.QLineEdit(self)
		ent_path_encode = qtw.QTextEdit(self)
		ent_path_encode.setReadOnly(1)
		ent_dir_decode = qtw.QLineEdit(self)
		ent_path_decoded = qtw.QLineEdit(self)
		ent_path_decode = qtw.QTextEdit(self)
		ent_path_decode.setReadOnly(1)

		btn_browse_dir_encode = qtw.QPushButton('Browse', self)
		btn_browse_dir_encode.clicked.connect(encode_source)
		btn_browse_path_encoded = qtw.QPushButton('Browse', self)
		btn_browse_path_encoded.clicked.connect(encoded_destination)
		btn_browse_encode_files = qtw.QPushButton('Browse', self)
		btn_browse_encode_files.clicked.connect(browse_encode_files)
		btn_browse_dir_decode = qtw.QPushButton('Browse', self)
		btn_browse_dir_decode.clicked.connect(decode_source)
		btn_browse_path_decoded = qtw.QPushButton('Browse', self)
		btn_browse_path_decoded.clicked.connect(decoded_destination)
		btn_browse_decode_files = qtw.QPushButton('Browse', self)
		btn_browse_decode_files.clicked.connect(browse_decode_files)

		frm_encode_decode_footer = qtw.QFrame()
		btn_encode = qtw.QPushButton('Encode', self)
		btn_encode.clicked.connect(encode_function)
		btn_decode = qtw.QPushButton('Decode', self)
		btn_decode.clicked.connect(decode_function)

		#Encode & Decode Layout
		layout_encode = qtw.QGridLayout()
		layout_encode.setColumnMinimumWidth(0, 100)
		frm_encode_decode.setLayout(layout_encode)
		layout_encode_decode.addWidget(frm_encode_decode)

		layout_encode.addWidget(lbl_dir_encode, 0, 0)
		layout_encode.addWidget(lbl_path_encoded, 1, 0)
		layout_encode.addWidget(lbl_path_encode, 2, 0)
		layout_encode.addWidget(lbl_dir_decode, 3, 0)
		layout_encode.addWidget(lbl_path_decoded, 4, 0)
		layout_encode.addWidget(lbl_path_decode, 5, 0)

		layout_encode.addWidget(ent_dir_encode, 0, 1)
		layout_encode.addWidget(ent_path_encoded, 1, 1)
		layout_encode.addWidget(ent_path_encode, 2, 1)
		layout_encode.addWidget(ent_dir_decode, 3, 1)
		layout_encode.addWidget(ent_path_decoded, 4, 1)
		layout_encode.addWidget(ent_path_decode, 5, 1)

		layout_encode.addWidget(btn_browse_dir_encode, 0, 2)
		layout_encode.addWidget(btn_browse_path_encoded, 1, 2)
		layout_encode.addWidget(btn_browse_encode_files, 2, 2)
		layout_encode.addWidget(btn_browse_dir_decode, 3, 2)
		layout_encode.addWidget(btn_browse_path_decoded, 4, 2)
		layout_encode.addWidget(btn_browse_decode_files, 5, 2)

		layout_encode_decode_footer = qtw.QHBoxLayout()
		frm_encode_decode_footer.setLayout(layout_encode_decode_footer)
		layout_encode_decode_footer.addWidget(btn_encode)
		layout_encode_decode_footer.addWidget(btn_decode)
		layout_encode_decode.addWidget(frm_encode_decode_footer)

		#Settings Content
		lbl_dir_pak_builder = qtw.QLabel('PakBuilder Path', self)
		lbl_dir_pak_unpacker = qtw.QLabel('PakUnpacker Path', self)
		lbl_dir_encoder = qtw.QLabel('Encoder Path', self)

		ent_dir_pak_builder = qtw.QLineEdit(self)
		ent_dir_pak_unpacker = qtw.QLineEdit(self)
		ent_dir_encoder = qtw.QLineEdit(self)

		btn_browse_pak_builder = qtw.QPushButton('Browse', self)
		btn_browse_pak_builder.clicked.connect(browse_pak_builder)
		btn_browse_pak_unpacker = qtw.QPushButton('Browse', self)
		btn_browse_pak_unpacker.clicked.connect(browse_pak_unpacker)
		btn_browse_encoder = qtw.QPushButton('Browse', self)
		btn_browse_encoder.clicked.connect(browse_encoder)

		frm_settings_footer = qtw.QFrame()

		#Settings Layout
		layout_settings.addWidget(lbl_dir_pak_builder, 0, 0)
		layout_settings.addWidget(lbl_dir_pak_unpacker, 1, 0)
		layout_settings.addWidget(lbl_dir_encoder, 2, 0)

		layout_settings.addWidget(ent_dir_pak_builder, 0, 1)
		layout_settings.addWidget(ent_dir_pak_unpacker, 1, 1)
		layout_settings.addWidget(ent_dir_encoder, 2, 1)

		layout_settings.addWidget(btn_browse_pak_builder, 0, 2)
		layout_settings.addWidget(btn_browse_pak_unpacker, 1, 2)
		layout_settings.addWidget(btn_browse_encoder, 2, 2)

		layout_settings.addWidget(frm_settings_footer)

		#Message Popup for Functions
		global msg_box
		msg_box = qtw.QMessageBox()

		#Stylesheet
		stylesheet = 'gui.css'
		with open(stylesheet, 'r') as fh:
			self.setStyleSheet(fh.read())

		#Check File Paths
		def builder_path_check():
			if os.path.isfile('pakfilebuilder_path.txt'):
				builder_path = open('pakfilebuilder_path.txt', 'r').read()
				ent_dir_pak_builder.clear()
				ent_dir_pak_builder.setText(builder_path)
			else:
				pass

		def unpacker_path_check():
			if os.path.isfile('pakfileunpacker_path.txt'):
				unpacker_path = open('pakfileunpacker_path.txt', 'r').read()
				ent_dir_pak_unpacker.clear()
				ent_dir_pak_unpacker.setText(unpacker_path)
			else:
				pass

		def encoder_path_check():
			if os.path.isfile('ddsencoder_path.txt'):
				encoder_path = open('ddsencoder_path.txt', 'r').read()
				ent_dir_encoder.clear()
				ent_dir_encoder.setText(encoder_path)
			else:
				pass		

		builder_path_check()
		unpacker_path_check()
		encoder_path_check()

		#End Main UI Code
		self.show()

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec())
