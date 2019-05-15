import matplotlib.pyplot as plt
summe = 0
schachbrett =[]

for feld in range(64):
    reiskorn = 2**feld
    schachbrett.append(reiskorn)
    summe += reiskorn # ist das Gleiche wie summe = summe + reiskorn
    gewicht = summe * 0.02 / 1000 / 1000 # ein Reiskorn wiegt 0,2 gramm

    #{:>2} bedeutet= : steht für alle zeichen, > heißt rechtsbündig, 25 steht für die Anzahl der zeichen udn das Komma steht für die tausender trennung
    #print("Feld: {:>2}. = {:>25,} Reiskörner und damit insgesamt {:>26,} Reiskörner".format(feld+1, reiskorn, summe))

    # hier steht das f für einen sogenannten f-string. Damit entfällt das .format() am ende des Strings udn man schreibt das Format gleich ind den Platzhalter
    print(f"Feld: {feld+1:>2}. = {reiskorn:>25,} Reiskörner und damit insgesamt {summe:>26,} Reiskörner")

# .1f steht für 1 stelle der fliesskommazahl
print(f"Das sind {gewicht:16,.1f} Tonnen")
#https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
plt.plot(schachbrett)
plt.show()