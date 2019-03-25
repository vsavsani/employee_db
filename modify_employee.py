import methods

def modify_employee(file_n):
	print("Modifying Employee")
	file_h = methods.open_for_read(file_n)
	if (methods.check_for_entry(file_h, e_data[0])):
		
	methods.load_emp_data(file_h)