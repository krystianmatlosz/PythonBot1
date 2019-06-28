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


if user_choice == "imię":
    imie()

elif user_choice == "matma":
    matma()