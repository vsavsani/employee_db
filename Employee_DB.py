import pickle
import Employee
def main():
  emp_dic = load_emp()
  menu()
  choice = input('Enter your choice')
  while choice!=5:
    if choice == 1:
        add_(emp_dic)
    elif choice == 2:
        change(emp_dic)
    elif choice == 3:
        dele_(emp_dic)
    elif choice ==4:
        lookup(emp_dic)
    elif choice <= 0 or  choice > 5:
        print 'You made a wrong selection'
    elif choice == 5:
        print "The program would quit now..."
    print''
    print''
    menu()
    choice = input('Enter your choice')
    save_emp(emp_dic)        


def load_emp():
  try:
    load_dic = open('employee.dat' , 'rb')
    emp_details = pickle.load(load_dic)
    load_dic.close()
  
  except IOError:
    emp_details = {}
  return emp_details

def save_emp(emp_dic):
  save_file = open('employee.dat','wb')
  pickle.dump(emp_dic , save_file)
  save_file.close()

def lookup(emp_dic):
  search = raw_input("Enter your search query")
  search_result = emp_dic.get(search, "Entry not found")
  print search_result

def add_(emp_dic):
  
  again = 'y'
  while again.lower() == 'y':
    number = raw_input("Enter the ID number: ")
    name_ = raw_input("Enter employee name: ")
    mobile = raw_input("Enter Mobile No.: ")
    landline = raw_input("Enter Lnadline No.: ")
    if number not in emp_dic:
        entry = Employee.Employee(number ,name_, mobile, landline)
        emp_dic[name_]  = entry
        print name_, "has been successfully added"
    else:
        print name_, "already exists!"
    again = raw_input("Enter 'y' to continue or any other alphabet to quit")

def change(emp_dic):
  search = raw_input("Enter the name you want to change the details")
  if search in emp_dic:
    name_ = raw_input("Enter new employee name")
    number = raw_input("Enter new the ID number")
    depart = raw_input("Enter new Department")
    job = raw_input("Enter new Job title")
    entry = Employee(name_,number, depart, job)
    emp_dic[name_]  = entry
    print name_, "has been successfully updated"
  else:
    print "Entry not found"

def delete_ (emp_dic):
  search = raw_input("Enter the name you want to change the details")
  if search in emp_dic:
    del emp_dic[search]
    print search, " has been deleted successfully"
  else:
    print "Entry not found"

def menu():
  print 'Choose your Option below'
  print 'Add new Employee Details = 1'
  print 'Change an existing Employee Details = 2'
  print 'Delete an Employee Details = 3'
  print "Look-up Employee Details = 1"
  print 'Quit the program = 5'


main()
