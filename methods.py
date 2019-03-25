import os
from os import path

def load_emp_data(file_h):
	line = file_h.readline()
	entry = line.split(',')
	emp_dict = {}
	while line:
		emp_dict[entry[0]] = {	
								'name':entry[1],
								'contacts': {
									'mobile':(entry[2],entry[3]),
									'landline':(entry[4],entry[5].strip())
								}
							};
		print(emp_dict)
		line = file_h.readline()
		entry = line.split(',')

	return emp_dict

def open_for_read(file_n):
	if not(path.exists(file_n)):
		open(file_n,'a').close()
	return open(file_n,'r')

def open_for_write(file_n):
	if (path.exists(file_n)):
		file_h = open(file_n,'a')
	else:
		file_h = open(file_n,'w+')
	return file_h

def check_for_entry(file_h, key):
	if key in file_h.read():
		return True;
	return False;

def write_entry(file_h, data):
	file_h.write(','.join(data))
	file_h.write("\n")
