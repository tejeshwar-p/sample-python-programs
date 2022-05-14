# Giraffe Language
# Vowels are replaced with 'g'
# Ex - dog -> dgg
#    - cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate("This is some sample text"))
print(translate(input("Enter some text: ")))

