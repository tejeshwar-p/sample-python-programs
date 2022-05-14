is_male = True
is_tall = True

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")
is_male = True
if is_male and is_tall:
    print("You are a tall male")

is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are not a male but are tall")
