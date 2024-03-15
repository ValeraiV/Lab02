import dictionary as dy
d = dy.Dictionary()
dizionario = {}

class Translator:
    def __init__(self):
        self.d = d

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")

    def loadDictionary(self, diz):
        # dict is a string with the filename of the dictionary
        with open(diz) as file:
            for parola in file:
                a = parola.split()
                d.dizionario[a[0]] = a[1:]


    def handleAdd(self, entry):
        with open("dictionary.txt", "a") as file:
            file.write('\n' + entry)
            a = entry.split()
            d.addWord(a[0], a[1:])

        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        with open("dictionary.txt", "r") as file:
            for parola in file:
                a = parola.split()
                if query == str(a[0]):
                    print(a[1].split())
                    dy.translate = a[1]
        # query is a string <parola_aliena>

        pass

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass
