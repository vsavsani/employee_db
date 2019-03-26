import methods

def delete_employee(file_n, emp_id):
	print("Delete particular contact number")

	if (methods.check_for_entry(methods.open_for_read(file_n), emp_id)):

		emp_dict = methods.load_emp_data(methods.open_for_read(file_n), emp_id)

		choose_option()
		choice = int(input('Enter your choice: '))	
		if choice == 1:
			print(emp_dict[emp_id]['contacts']['mobile'][0])
			emp_dict[emp_id]['contacts']['mobile'][0] = '-'
			print(emp_dict[emp_id]['contacts']['mobile'][0])

			print(emp_dict)
			
			file_h = methods.open_new(file_n)
			methods.write_emp_data(file_h, emp_dict)
		elif choice == 2:
			print(emp_dict[emp_id]['contacts']['mobile'][1])
			emp_dict[emp_id]['contacts']['mobile'][1] = '-'
			print(emp_dict[emp_id]['contacts']['mobile'][1])

			print(emp_dict)

			file_h = methods.open_new(file_n)
			methods.write_emp_data(file_h, emp_dict)
		elif choice == 3:
			print(emp_dict[emp_id]['contacts']['landline'][0])
			emp_dict[emp_id]['contacts']['landline'][0] = '-'
			print(emp_dict[emp_id]['contacts']['landline'][0])

			print(emp_dict)

			file_h = methods.open_new(file_n)
			methods.write_emp_data(file_h, emp_dict)
		elif choice == 4:
			print(emp_dict[emp_id]['contacts']['landline'][1])
			emp_dict[emp_id]['contacts']['landline'][1] = '-'
			print(emp_dict[emp_id]['contacts']['landline'][1])
			print(emp_dict)
			file_h = methods.open_new(file_n)
			methods.write_emp_data(file_h, emp_dict)
		else:
			print('Invalid Input')


	else:		

		print("Employee ID not present.")

def choose_option():
	print("Choose any option: ")
	print("1. Mobile 1")
	print("2. Mobile 2")
	print("3. Landline 1")
	print("4. Landline 2")