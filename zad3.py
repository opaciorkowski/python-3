import random

t = ["Papier", "Kamień", "Nożyce"]
singleplayer = 1
p1score = 0
p2score = 0
print("Wybierz tryb \n1. Hotseat\n2. Solo ")
gamemode = int(input())
match gamemode:
    case 1:
        singleplayer = 0
        print("wybrales hotseat")
    case 2:
        singleplayer = 1
        print("wybrales solo")
    case _:
        print("niepoprawny wybór")
        exit()
p1 = input("Podaj nazwę pierwszego gracza \n")
if singleplayer == 0:
    p2 = input("Podaj nazwę drugiego gracza \n")
else:
    p2 = "robot"

rounds = int(input("ile rund?"))
i = 0
while i < rounds:
    print("Aktualny wynik:\n", p1, p1score, " | ", p2, p2score)
    print(p1, "wybiera")
    choice1 = input("1.Papier\n2.Kamień\n3.Nożyce\n")
    print("====")
    print(p2, "wybiera")
    if singleplayer == 0:
        choice2 = input("1.Papier\n2.Kamień\n3.Nożyce\n")
    else:
        choice2 = random.randint(1, 3)
        print(choice2)
    if choice1 == choice2:
        print('Remis')
        p1score += 1
        p2score += 1
    if choice1 == 1:
        if choice2 == 2:
            print("Wygral", p1)
            p1score += 1
        elif choice2 == 3:
            print("Wygral", p2)
            p2score += 1

    if choice1 == 2:
        if choice2 == 3:
            print("Wygral", p1)
            p1score += 1
        elif choice2 == 1:
            print("Wygral", p2)
            p2score += 1

    if choice1 == 3:
        if choice2 == 1:
            print("Wygral", p1)
            p1score += 1
        elif choice2 == 2:
            print("Wygral", p2)
            p2score += 1
    i += 1
if (p1score > p2score):
    print("Wygral", p1)
elif (p1score < p2score):
    print("Wygral", p2)
else:
    print("Remis po wszystkich rundach")
