# Bardzo osobisty bot zrobiony przeze mnie

botName = "Alex"
print("Cześć, tutaj bot", botName)

user_choice = input("Co mam zrobić? ")

def imie():
    newName = input("Podaj imię: ")
    print("Cześć, z tej strony", newName)

def matma():
        print("No hej, coś Ci poobliczam")
        a = int(input("Podaj a:"))
        b = int(input("Podaj b:"))
        matma_ab(a,b)

def matma_ab(a,b): 
    print("a + b = ", a+b)
    print("a - b = ", a-b)
    print("a ^ b = ", a**b)

def polacz():
    napis1 = input("Podaj 1 napis: ")
    napis2 = input("Podaj 2 napis: ")
    print(polacz_ab(napis1,napis2))

def polacz_ab(a,b):
    c = a + b 
    return c

def lista_zakupow():
    a = []
    for i in range(3):
        item = input("Co mam kupić? ")
        a.append(item)
    print("Lista zakupów: ", a)
    w_liscie(a)

def w_liscie(a):
    for item in a:
        print("Zapisałem: ", item)
    print("Koniec listy")

def notatki():
    number = input("Liczba notatek: ")
    d = {}
    




if user_choice == "imię":
    imie()

elif user_choice == "matma":
    matma()

elif user_choice == "połącz":
    polacz()

elif user_choice == "zakupy":
    lista_zakupow()