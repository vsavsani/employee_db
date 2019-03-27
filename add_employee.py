import methods
import re 
def add_employee(emp_data_file):
	print('\n')
	print('*******Adding Employee*******')
	
	emp_dict = add_menu()

	file_h = methods.open_for_read(emp_data_file)
	key = list(emp_dict.keys())[0]
	if not(methods.check_for_entry(file_h, key)):

		'''Printing added employees details'''
		print('\nAdded Employees Details: ')
		print(emp_dict)

		'''Adding data to the file'''
		file_h = methods.open_for_write(emp_data_file)
		for key in emp_dict.keys():
			line = key + "," + emp_dict[key]['name'] + ","  + emp_dict[key]['contacts']['mobile'][0] + "," + emp_dict[key]['contacts']['mobile'][1] + "," + emp_dict[key]['contacts']['landline'][0] + "," + emp_dict[key]['contacts']['landline'][1]
		file_h.write(line+"\n")
		file_h.close()
	else:
		print("Entry already exists...")

def add_menu():

	'''Fetching data from User'''
	e_data = [None]*6

	e_data[0] = input('Employee id: ')
	if not(re.search(r"^\d{6}$",e_data[0])):
		print('Employee ID should be integer and of length 6.')
		emp_dict = add_menu()
		return emp_dict

	e_data[1] = input('Employee name: ')
	if not(re.search(r"[a-zA-Z]+",e_data[1])):
		print('Employee name should be alphabetic.')
		emp_dict = add_menu()
		return emp_dict

	e_data[2] = input('Employee mobile1: ')
	if not(re.search(r"^\d{10}$|-",e_data[2])):
		print('Employee mobile no. 1 should be integer of length 10 or -')
		emp_dict = add_menu()
		return emp_dict

	e_data[3] = input('Employee mobile2: ')
	if not(re.search(r"^\d{10}$|-",e_data[3])):
		print('Employee mobile no. 2 should be integer of length 10 or -')
		emp_dict = add_menu()
		return emp_dict

	e_data[4] = input('Employee landline1: ')
	if not(re.search(r"^\d{10}$|-",e_data[4])):
		print('Employee landline no. 1 should be integer of length 10 or -')
		emp_dict = add_menu()
		return emp_dict

	e_data[5] = input('Employee landline2: ')
	if not(re.search(r"^\d{10}$|-",e_data[5])):
		print('Employee landline no. 2 should be integer of length 10 or -')
		emp_dict = add_menu()
		return emp_dict

	emp_dict = {}
	emp_dict[e_data[0]] = {'name':e_data[1], 'contacts': { 'mobile':[e_data[2],e_data[3]], 'landline':[e_data[4],e_data[5]]}}
	
	return emp_dict
