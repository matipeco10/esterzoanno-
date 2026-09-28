"""
data una lista di 20 elementidi temperature randomiche nell'interavallo -20,+40 calcolare il numero di elementi sopra lo zero,
sotto lo zero è stampare la scritta freddo estremo se le temperature sotto lo 0 superano quelle sopra lo 0. Caldo estremo nell'altro
caso
"""
import random
lista=[]
for i in range (0,20):
    lista.append(random.randint(-20,+40))
caldoestremo=0
freddoestremo=0
for i in range (0,20) :
    if lista [i]>0:
        caldoestremo=caldoestremo+1
    else :
        freddoestremo=freddoestremo+1
if caldoestremo>freddoestremo :
    print("caldo estremo")
else:
    print("freddoestremo")
    



