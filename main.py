from random import randrange

print("Chemie Alkan(ol) Generator")
while 1:
    a = input("Alkan oder Alkanol? ")
    if a == "Alkan":
        kmin = int(input("Kettenlänge minimal: "))
        kmax = int(input("Kettenlänge maximal: "))
        print("Kettenlänge von ", kmin, " bis ", kmax)
        if kmin <= 0:
            kmin = 1
        if kmax >= 7:
            kmax = 6
        k = randrange(kmin, kmax, 1)  # kettenlänge
        e = input("Ethyl? Y/N ")
        if e == "Y" or e == "y":
            e = 1
        if e == "N" or e == "n":
            e = 0
        skmin = int(input("Minimale Seitenketten: "))
        skmax = int(input("Maximale Seitenketten: "))
        if skmin <= -1:
            skmin = 0
        if skmax >= 5:
            skmax = 4
        s = randrange(skmin, skmax, 1)  # seitenketten
        alkan = ["famous zero", "Methan", "Ethan", "Propan", "Butan", "Pentan", "Hexan"]
        yl = ["famous zero", "methyl", "ethyl"]
        bigyl = ["famous zero", "Methyl", "Ethyl"]  # listen für den print
        nalkan = ["famous zero", "This will not generate", "This neither", "propan", "butan", "pentan"]
        zahl = ["Haha NERD", "", "Di", "Tri", "Tetra"]
        if s == 0 or k <= 2:
            print(alkan[k - 1])  # bei k <= 2 kein platz für seitenketten
        elif s >= 1:
            if e == 1:
                print("WIP")
            else:

                if k == 3:  # else randint(2, 2, 1) --> Error
                    sk1p = 2
                    sk2p = 2
                    if s >= 3:
                        s = 2
                    if s == 1:
                        print(sk1p, " - ", bigyl[1], nalkan[k])
                    elif s == 2:
                        print(sk1p, ", ", sk2p, " - ", zahl[2], yl[1], nalkan[k])
                    break

                sk1p = int(randrange(2, k - 1, 1))
                sk2p = int(randrange(2, k - 1, 1))
                full = 0
                if sk1p == sk2p:
                    full = sk1p
                sk3p = int(randrange(2, k - 1, 1))
                while sk3p == full:  # nur 2 seitenketten pro c - atom
                    sk3p = int(randrange(2, k - 1, 1))
                sk4p = int(randrange(2, k - 1, 1))
                while sk4p == full:
                    sk4p = int(randrange(2, k - 1, 1))

                if s == 1:
                    print(sk1p, " - ", bigyl[1], nalkan[k])
                elif s == 2:
                    print(sk1p, ", ", sk2p, " - ", zahl[2], yl[1], nalkan[k])
                elif s == 3:
                    print(sk1p, ", ", sk2p, ", ", sk3p, " - ", zahl[3], yl[1], nalkan[k])
                elif s == 4:
                    print(sk1p, ", ", sk2p, ", ", sk3p, ", ", sk4p, " - ", zahl[4], yl[1], nalkan[k])
                break







    elif a == "Alkanol":
        a = "Alkanol"
    elif a == "exit":
        break
