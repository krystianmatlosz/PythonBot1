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

if text == "matma":
    matma()

elif text == "imię":
    imię()

elif text == "połącz":
    połącz()

elif text == "zakupy":
    lista_zakupow()

else:
    print("Nie wiem co mam zrobić")

