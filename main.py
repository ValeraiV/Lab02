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

        try:
            txt2In = str(input().lower())
            print(txt2In)

            if txt2In.replace(" ", "").isalpha():
                t.handleAdd(txt2In)
                print(txt2In.split())
                print("Aggiunta!")

            else:
                print("Parola errata")

        except Exception:
            print("Errore, parola non trovata")


    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        try:
            txt2In = input().lower()
            if txt2In.isalpha():
                a = ''
                for i in t.handleTranslate(str(txt2In)):
                    a += i
                print(f"La traduzione è: {a}")
            else:
                print("Parola errata")

        except Exception:
            print("Errore, parola non trovata")

    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        try:
            txt2In = input().lower()
            a = ''
            for i in t.handleWildCard(str(txt2In)):
                a += i
            print(f"La traduzione è: {a}")

        except Exception:
            print("Errore, parola non trovata")



    elif int(txtIn) == 4:
        break

    else:
        print("Codice errato")
