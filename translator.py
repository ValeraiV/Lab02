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
        print("4. Exit")

    def loadDictionary(self, diz):
        # dict is a string with the filename of the dictionary
        with open(diz) as file:
            for parola in file:
                a = parola.split()
                d.dizionario[a[0]] = a[1:]


    def handleAdd(self, entry):
            a = entry.split()
            d.addWord(a[0], a[1:])
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        return(d.translate(query))
        # query is a string <parola_aliena>

    def handleWildCard(self, query):
        return(d.translateWordWildCard(query))
        # query is a string with a ? --> <par?la_aliena>
