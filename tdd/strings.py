def Formatting(first_name, last_name):
    return f"His name is {first_name} {last_name}."

def NoSpace(text):
    no_space = ""
    for char in text:
        if char != " ":
            no_space+= char
    return no_space

def TextLenght(text):
    return len(text)
