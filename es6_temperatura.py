"""
Stampare lo stato di aggregazione dell 'acqua data la sua temperatura in input
"""
temperatura=input("inserisci la temperatura del campione d'acqua")
temperatura=float(temperatura)
if temperatura<=0 :
    print("il campione si trova allo stato solido")
elif temperatura > 0 and temperatura <= 100:
        print ("il campione si trova allo stato liquido")
else :
    print("il campione si trova allo stato gassoso") 