def check_for_entry(file_h, str):
	if str in file_h.read():
		return True;
	return False;

print(check_for_entry(open('employee.csv','r'), "aaa"))