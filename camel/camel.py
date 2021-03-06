def display_banner():
    """ Display program name in banner """
    msg = 'camelCase converter'
    stars = "*" * len(msg)
    print( '\n' + stars + '\n' + msg + '\n' + stars + '\n\n')


def ask_for_string():
    return input("please enter a string to camelify: \n")


def ify(text=""):
    camelfied = ""
    lower_text = text.lower()
    split_text = [word for word in lower_text.split(" ") if len(word) > 0]
    for word in split_text:
        if len(word) > 1:
            camelfied += word[0].upper() + word[1:]
        else:
            camelfied += word[0].upper()
    return camelfied[0].lower() + camelfied[1:]


if __name__ == '__main__':
    display_banner()
    string = ask_for_string()
    print(ify(string))
