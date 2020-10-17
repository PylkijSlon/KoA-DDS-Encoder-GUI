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
				path = ent_dir_pak.text() + '/'
				input_list = ent_pak_create.text() + '.txt'
				dirs = os.listdir(path)
				with open(input_list, 'w', encoding='utf-8') as f:
					for item in dirs:
						f.write(path + "%s\n" % item)

		#Pack
		def create_pak(): 
			input_list()
			builder = ent_dir_pak_builder.text()
			input_list = os.path.abspath(ent_pak_create.text()) + ".txt"
			pak = ent_pak_create.text() + ".pak"

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

			elif ent_data_dir.get() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the data directory where the .pak file is located.")
				return

			elif ent_pak_name.get() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the name of the .pak file you wish to unpack.")
				return
    
			elif ent_target_dir.get() == '':
				qtw.QMessageBox.information(self, "Error", "Please set the directory you wish to unpack into.")
				return

			else:
				unpacker = ent_dir_pak_unpacker.text()
				path = ent_dir_data.text() + "/"
				pak = ent_pak_name.text() + ".pak"
				target = ent_dir_target.text() + "/"

				try:
					unpacker_unpack = subprocess.Popen([unpacker, path + pak, 'unpack', target],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

				except Exception as ex:
					print(ex)
    
				else:
					print(unpacker_unpack.communicate())
		#List
		def list_pak():
			if ent_dir_pak_unpacker.text() == "":
				qtw.QMessageBox.information(self, "Error", "Please set the directory of the pakfileunpacker.exe")
				return

			elif ent_dir_data.text() == "":
				qtw.QMessageBox.information(self, "Error", 'Please set the data directory where the .pak file is located.')
				return

			elif ent_pak_name.text() == "":
				qtw.QMessageBox.information(self, "Error", "Please set the name of the .pak file you wish to list the contents of.")
				return

			else:
				unpacker = ent_dir_pak_unpacker.text()
				path = ent_dir_data.text() + "/"
				pak = ent_pak_name.text() + ".pak"
				pak_list_file = ent_pak_name.text() + ".txt"

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
			msg_box = qtw.QMessageBox()

			if ent_path_encoded.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please set the target directory')

			elif ent_path_encode.toPlainText() == '':
				title = 'Encoding Directory'
				msg = 'Encoding your .dds Files from Standard Format to KoA Format. Please be patient.'
				msg_box.setText(title)
				msg_box.setInformativeText(msg)
				msg_box.exec_()
				encode_dir()

			else:
				title = 'Encoding Files'
				msg = 'Encoding your .dds Files from Standard Format to KoA Format. Please be patient.'
				msg_box.setText(title)
				msg_box.setInformativeText(msg)
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
				encode = subprocess.Popen([encoder, '2', filepath],
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
				encode = subprocess.Popen([encoder, '2', filepath],
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
				print(encode.communicate())
				encode.terminate()

		def decode_function():
			msg_box = qtw.QMessageBox()
			
			if ent_path_decoded.text() == '':
				qtw.QMessageBox.information(self, 'Error', 'Please set the target directory')

			elif ent_path_decode.toPlainText() == '':
				title = 'Decoding Directory'
				msg = 'Decoding your .dds Files from KoA Format to Standard. Please be patient.'
				msg_box.setText(title)
				msg_box.setInformativeText(msg)
				msg_box.exec_()
				decode_dir()

			else:
				title = 'Decoding Files'
				msg = 'Decoding your .dds Files from KoA Format to Standard. Please be patient.'
				msg_box.setText(title)
				msg_box.setInformativeText(msg)
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
				decode = subprocess.Popen([encoder, '1', item],
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

		def patch_source():
			patch = qtw.QFileDialog.getExistingDirectory()
			ent_path_en_source.clear()
			ent_path_en_source.setText(patch)
			with open('sourcePatch.txt', 'w') as f:
				f.write(patch)

		def data_source():
			data = qtw.QFileDialog.getExistingDirectory()
			ent_path_en_source.clear()
			ent_path_en_source.setText(data)
			with open('sourceData.txt', 'w') as f:
				f.write(data)

		def initial_source():
			initial = qtw.QFileDialog.getExistingDirectory()
			ent_path_en_source.clear()
			ent_path_en_source.setText(initial)
			with open('sourceInitial.txt', 'w') as f:
				f.write(initial)

		def set_target():
			target = qtw.QFileDialog.getExistingDirectory()
			ent_path_en_target.clear()
			ent_path_en_target.setText(target)
			with open('targetPath.txt', 'w') as f:
				f.write(target)

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
		lbl_main_intro = qtw.QLabel('This is a very alpha version created to match the release of the KoA Encoding/Decoding tools by Szlobi. Currently, error reporting is minimal and there are only a few checks to ensure that the correct data has been entered.', 
			self
		)
		lbl_main_intro.setWordWrap(1)
		lbl_main_packaging = qtw.QLabel('Packaging: The app can package a directory into a KoA .pak file using the modding tools provided by the developer. To do so, select the directory you wish to pack via the browse button and enter a .pak name (omitting the .pak at the end). In addition, you must set the directory path for the pakfilebuilder.exe, located in the KoA game directory in the modding folder. If the file is large, the app will appear to hang and do nothing. However, the pakfilebuilder.exe will be working in the background and a list of the files packed will appear in the terminal upon completion. An update will come soon with progress indication.', 
			self
		)
		lbl_main_packaging.setWordWrap(1)
		lbl_main_unpacking = qtw.QLabel('Unpacking: The app can unpackage a KoA .pak file into a directory using the modding tools provided by the developers. To do so, select the KoA Data directory, a directory you wish to unpack the files into and name the .pak you wish to unpack (omitting the .pak at the end of the name. In addition, you must set the directory path for the pakfileunpacker.exe, located in the KoA game directory in the modding folder. If the file is large, the app will appear to hang and do nothing. However, the pakfileunpacker.exe will be working in the background. However, it will not output any information to the terminal upon completion.', 
			self
		)
		lbl_main_unpacking.setWordWrap(1)
		lbl_main_encoding = qtw.QLabel('WIP', 
			self
		)
		lbl_main_decoding = qtw.QLabel('WIP',
			self
		)

		layout_main.addWidget(lbl_main_intro)
		layout_main.addWidget(lbl_main_packaging)
		layout_main.addWidget(lbl_main_unpacking)
		layout_main.addWidget(lbl_main_encoding)
		layout_main.addWidget(lbl_main_decoding)

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
		btn_create_pak.clicked.connect(input_list)

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

		ent_dir_data = qtw.QLineEdit(self)
		ent_dir_target = qtw.QLineEdit(self)
		ent_pak_unpack = qtw.QLineEdit(self)

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

		layout_unpack.addWidget(ent_dir_data, 0, 1)
		layout_unpack.addWidget(ent_dir_target, 1, 1)
		layout_unpack.addWidget(ent_pak_unpack, 2, 1)

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

		#Stylesheet
		stylesheet = 'appstyle.css'
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