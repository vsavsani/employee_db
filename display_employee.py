import re
import methods

def display_employee(file_n):
	print("Display the Employee details ")
	#if (methods.check_for_entry(methods.open_for_read(file_n), emp_id))
	emp_dict = methods.load_emp_data(methods.open_for_read(file_n))
	choose_option()
	choice = int(input('Enter your choice: '))	
	if choice == 1:
		emp_id = input('Enter Employee ID: ')
		if (methods.check_for_entry(methods.open_for_read(file_n), emp_id)):
			print(emp_dict[emp_id])
		else:
			print('Employee ID not present.')
	elif choice == 2:
		pattern= input(str("enter pattern: "))
		for key in emp_dict.keys():
			name=emp_dict[key]['name']
			res = name.find(pattern)
			if(res>=0):
				print(emp_dict[key])
			else:
				continue
	else:
		print('Invalid Input')

def choose_option():
	print("Choose any option: ")
	print("1. Display by employee id")
	print("2. Display by String")
