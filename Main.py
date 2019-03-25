import add_employee
import modify_employee
import delete_employee
import display_employee


employee_data_file = "D:\\source\\vibha\\employee_db\\employee.csv"

def main():
  menu()
  choice = int(input('Enter your choice'))
  while choice!=5:
    if choice == 1:
        add_employee.add_employee(employee_data_file)
    elif choice == 2:
        modify_employee.modify_employee(employee_data_file)
    elif choice == 3:
        delete_employee.delete_employee(employee_data_file)
    elif choice ==4:
        display_employee.display_employee(employee_data_file)
    elif choice <= 0 or  choice > 5:
        print("You made a wrong selection")
    elif choice == 5:
        print("The program would quit now...")
    menu()
    choice = int(input('Enter your choice'))

def menu():
  print('Choose your Option below')
  print('Add new Employee Details = 1')
  print('Change an existing Employee Details = 2')
  print('Delete an Employee Details = 3')
  print("Look-up Employee Details = 4")
  print('Quit the program = 5')


#################################################
main()