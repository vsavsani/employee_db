import os
from os import path

def load_emp_data(file_h, emp_id):
	line = file_h.readline()
	#print(line)
	entry = line.split(',')
	emp_dict = {}
	while line:			
		emp_dict[entry[0]] = {	
								'name':entry[1],
								'contacts': {
									'mobile':[entry[2],entry[3]],
									'landline':[entry[4],entry[5].strip()]
								}
							};
		#print(emp_dict)
		line = file_h.readline()
		entry = line.split(',')
	file_h.close()
	print(emp_dict)
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

def open_new(file_n):
	return open(file_n,'w')

def check_for_entry(file_h, str):
	if str in file_h.read():
		file_h.close()
		return True
	file_h.close()
	return False;

def write_entry(file_h, data):
	file_h.write(','.join(data))
	file_h.write("\n")
	
'''
def update_entry(file_h, emp_id, new_no):
	line = file_h.readline()
	print(line)
	entry = line.split(',')

	while line:			
		if(entry[0]==emp_id):
			modified_data = line.replace(line,entry[0]+','+entry[1]+','+new_no+','+entry[3]+','+entry[4]+','+entry[5])
			file_h.write(modified_data)
			break;
		line = file_h.readline()
		entry = line.split(',')
'''
def write_emp_data(file_h, emp_dict):
	for key in emp_dict.keys():
		line = key + "," + emp_dict[key]['name'] + ","  + emp_dict[key]['contacts']['mobile'][0] + "," + emp_dict[key]['contacts']['mobile'][1] + "," + emp_dict[key]['contacts']['landline'][0] + "," + emp_dict[key]['contacts']['landline'][1]

		file_h.write(line+"\n")
	file_h.close()
