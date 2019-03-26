import add_employee
import modify_employee
import delete_employee
import display_employee


employee_data_file = "employee.csv"

def main():
  menu()
  choice = int(input('Enter your choice: '))
  while choice!=5:
    if choice == 1:
        add_employee.add_employee(employee_data_file)
    elif choice == 2:
        emp_id = input('Enter Employee ID: ')
        modify_employee.modify_employee(employee_data_file, emp_id)
    elif choice == 3:
        emp_id = input('Enter Employee ID: ')
        delete_employee.delete_employee(employee_data_file, emp_id)
    elif choice ==4:
        display_employee.display_employee(employee_data_file)
    elif choice <= 0 or  choice > 5:
        print("You made a wrong selection")
    elif choice == 5:
        print("The program would quit now...")
    menu()
    choice = int(input('Enter your choice'))

def menu():
  print('***************************************************')
  print('*                   Menu                          *')
  print('***************************************************')
  print('Choose your Option below')
  print('1. Add new Employee Details')
  print('2. Change an existing Employee Details')
  print('3. Delete an Employee Details')
  print('4. Look-up Employee Details')
  print('5. Quit the program')


#################################################
main()
