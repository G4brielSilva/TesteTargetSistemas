def invert(string):
    reversed_string = ""
    for i in range(len(string)-1, 0, -1):
        reversed_string += string[i]
    
    return reversed_string


if __name__ == "__main__":

    string_qualquer = "Oi sou uma string genérica"
    print(invert(string_qualquer))
