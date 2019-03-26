import methods
import re 
def add_employee(emp_data_file):
	print("Adding Employee")
	
	#emp_dict = load_emp_data(emp_data_file)
	emp_dict = add_menu()

	file_h = methods.open_for_read(emp_data_file)
	#if not(methods.check_for_entry(file_h, e_data[0])):
	key = list(emp_dict.keys())[0]
	if not(methods.check_for_entry(file_h, key)):
		#file_h.close()
		file_h = methods.open_for_write(emp_data_file)
		for key in emp_dict.keys():
			line = key + "," + emp_dict[key]['name'] + ","  + emp_dict[key]['contacts']['mobile'][0] + "," + emp_dict[key]['contacts']['mobile'][1] + "," + emp_dict[key]['contacts']['landline'][0] + "," + emp_dict[key]['contacts']['landline'][1]
		file_h.write(line+"\n")
		#methods.write_entry(file_h, e_data)
		file_h.close()
	else:
		print("entry already exists...")

def add_menu():
	e_data = [None]*6
	e_data[0] = input("employee id:")
	if not(re.search(r"\d+",e_data[0])):
		print('Employee ID should be integer.')
		menu()
		#return
	e_data[1] = input("employee name:")
	#print(e_data[0] + '-' + e_data[1])
	e_data[2] = input("employee mobile1:")
	e_data[3] = input("employee mobile2:")
	e_data[4] = input("employee landline1:")
	e_data[5] = input("employee landline2:")
	
	emp_dict = {}
	emp_dict[e_data[0]] = {'name':e_data[1], 'contacts': { 'mobile':[e_data[2],e_data[3]], 'landline':[e_data[4],e_data[5]]}}
	print(emp_dict)
	return emp_dict
	#return e_data
