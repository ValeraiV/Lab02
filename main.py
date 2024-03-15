import translator as tr
# import dictionary as dy

t = tr.Translator()
# d = dy.Dictionary()

while True:
    t.printMenu()
    t.loadDictionary("dictionary.txt")
    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input().lower()

        if txtIn[0].isalpha() and txtIn[1].isalpha():
            t.handleAdd(txtIn)
            #print(txtIn.split())
            print("Aggiunta!")

        else:
            print("Parola errata")

    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        if txtIn.isalpha():
            txtIn = input().lower()
            print(txtIn)
            #d.translate(str(txtIn))

        else:
            print("Parola errata")

    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")

    elif int(txtIn) == 4:
        print("Ok, ecco il dizionario")

    elif int(txtIn) == 5:
        break
