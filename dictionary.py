#import translator as tr
#t = tr.Translator()

dizionario = {}
class Dictionary:
    def __init__(self):
        self.dizionario = dizionario

    def addWord(self, parola, traduzione):
        dizionario[parola] = traduzione
        print (dizionario)


    def translate(self):
        #t.handleTranslate(parola_traduzione)
        pass

    def translateWordWildCard(self):
        #t.handleTranslate()
        pass

