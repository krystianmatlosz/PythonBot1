# Bardzo osobisty bot - Bob

bot_name = "Bettie"

print("Hej, jestem bot", bot_name)

text = input("Co mam zrobić? ")

def matma():
        a = int(input("podaj a: "))
        b = int(input("podaj b: "))
        matma_ab(a, b)

    
def matma_ab(a, b):
        print("a + b = ", a+b)
        print("a - b = ", a-b)
        print("a * b = ", a*b)
        print("a / b = ", a/b)
        print("a // b = ", a//b)
        print("a % b = ", a%b)
        print("a ** b = ", a**b)

def połącz():
    a = input("a:")
    b = input("b:")
    print(join_text(a, b))


def imię():
    user_name = input("Jak masz na imie? ")
    print("Cześć", user_name, " miło mi Cię poznać!")

def join_text(a, b):
    c = a + b
    return c 

def lista_zakupow():
    a = []                  #deklaracja listy
    for i in range(4):
        item = input("Co mam kupić?")
        a.append(item)
    print("Lista zakupów: ", a)
    w_liscie(a)

def w_liscie(a):
    for item in a:
        print("Zapisałem: ", item)
    print("Koniec listy")

def notatki():
    number = int(input("Liczba notatek:"))
    d = {}

    for i in range(number):
        note = input("Notatka: ")
        d[i] = note
    
    w_slowniku(d)

def w_slowniku(a):
    for key in a:
        print("Notatka", key+1, ": ", a[key])
    print("Koniec notatek")

def zgadnij():
    hidden_word = "ukryte"
    solved = False

    while not solved:
        user_word = input("Podaj słowo: ")

        if hidden_word == user_word:
            solved = True
        else:
            for letter in user_word:
                print("Literka", letter, ": ", letter in hidden_word)
        
    print("Zgadłeś! Gratuluję!")
    
    


if text == "matma":
    matma()

elif text == "imię":
    imię()

elif text == "połącz":
    połącz()

elif text == "zakupy":
    lista_zakupow()

elif text == "notatki":
    notatki()

elif text == "zgadnij":
    zgadnij()

else:
    print("Nie wiem co mam zrobić")

