import methods
def add_employee(emp_data_file):
	print("Adding Employee")
	
	#emp_dict = load_emp_data(emp_data_file)
	e_data = add_menu()

	file_h = methods.open_for_read(emp_data_file)
	if not(methods.check_for_entry(file_h, e_data[0])):
		file_h.close()
		file_h = methods.open_for_write(emp_data_file)
		methods.write_entry(file_h, e_data)
		file_h.close()
	else:
		print("entry already exists...")

def add_menu():
	e_data = [None]*6
	e_data[0] = input("employee id:")
	e_data[1] = input("employee name:")
	e_data[2] = input("employee mobile1:")
	e_data[3] = input("employee mobile2:")
	e_data[4] = input("employee landline1:")
	e_data[5] = input("employee landline2:")

	return e_data