from random import randint

arv = randint(1, 999)
arvamus = int(input("Arva, millist tuhandest väiksemat arvu ma mõtlen: "))

arvamiste_arv=0
def arvamine(arvamus, arvamiste_arv):
    arvamiste_arv+=1
    if arvamus == arv:
        print("Ära arvasid! Tubli!")
    elif arvamiste_arv<=10:
        if arv > arvamus:
            print("Minu arv on suurem!")
        else:
            print("Minu arv on väiksem!")
        arvamus = int(input("Arva veel kord: "))
        arvamine(arvamus, arvamiste_arv)
    else:
        print("Sa ei arvanud 10 korraga arvu ära. Kahju küll.")

arvamine(arvamus, arvamiste_arv)

