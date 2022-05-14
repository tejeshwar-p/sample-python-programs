# employee_file = open("employees.txt", "r")
# print(employee_file.read())

employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

# employee_file = open("employees.txt", "w")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

employee_file2 = open("employees2.txt", "w")
employee_file2.write("\nKelly - Customer Service")
employee_file.close()

