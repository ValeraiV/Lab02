dizionario = {}
class Dictionary:
    def __init__(self):
        self.dizionario = dizionario

    def addWord(self, parola, traduzione):
        if parola in dizionario:
            for i in traduzione:
                if dizionario[parola] == i:
                    print(f"La traduzione {i} è già esistente")
                else:
                    traduzione_multipla = dizionario[parola]+traduzione
                    dizionario[parola] = traduzione_multipla
                    print(f"La traduzione {i} è stata aggiunta")
        else:
            dizionario[parola] = traduzione

        with open("dictionary.txt", "w") as file:
            for chiave, valore in dizionario.items():
                a = ""
                for i in valore:
                    a += i + " "
                file.write(chiave+ " "+ a+ '\n')
        print(dizionario)

    def translate(self, parola):
        return dizionario[parola]

    def translateWordWildCard(self, parola):
        for chiave in dizionario.keys():
            a = list(chiave)
            a1 = list(parola)
            cont = 0
            for i in range(len(a)):
                if a[i] != a1[i] and a1[i] == '?':
                    cont += 1
            if cont == 1:
                return dizionario[chiave]


