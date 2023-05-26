from cls import clear

clear()
greet = 1

def mainSection():
    global greet
    if greet == 1:
        print("Command Python v.0.1\nCompiled 26-05-2023")
        greet = 0
    command = input("\n> ")

    if command.lower() == "exit":
        exit()
    elif command == "":
        mainSection()
    else:
        print("'"+command+"' is not a executable or a command.")
        mainSection()

mainSection()
