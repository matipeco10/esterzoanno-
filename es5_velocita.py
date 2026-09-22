"""
Scrivi un programma che :
1.chieda all'utente la distanza percorsa in (km) e il tempo (h)
2.calcola la velocità media
3.Stampa il risultato con due cifre decimali e indica l'unità di misura

"""


spazio=input("inserisci la distanza percorsa in km")
spazio=float(spazio)
tempo=input ("inserisci il tempo trascorso in h")
tempo=int(tempo)
velocita= spazio/tempo
velocita=round(velocita,2)
print ("la velocità vale")
print(velocita)
print("km/h") 
