employee_file = open("employees.txt", "r")
print(employee_file.readable())
print(employee_file.writable())
# print(employee_file.readline())
print("\n")
for line in employee_file.readlines():
    print(line)
employee_file.close()

