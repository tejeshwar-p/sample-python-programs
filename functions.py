# function is collection of code that performs a particular task.

def hi_func(name, age):
    # name = input("Input your name: ")
    print("Hello " + name + "!, You are " + str(age) + " years old")


# hi_func()

hi_func("Mike", 35)
hi_func("Mark", 40)


def cube(num_to_cube):
    return num_to_cube * num_to_cube * num_to_cube


print(cube(2))
print(cube(3))
result = cube(4)
print(result)

