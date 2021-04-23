print(" Laipni ludzam musu programma ")
print(" ")
print(" Programma varat parbaudît savas zinasanas par datora ietekmi uz veselibu ")
print("Ja atbilde ir Ja, ievadiet 1")
print("Ja atbilde ir Ne, ievadiet 2")
print(" ")

a=int(input( " Vai, jusuprat, ilgstoğs darbs ar datoru var butiski ietekmet cilveku veselibu? "))
if a == 1: print(" Ta ir taisniba, ka ar ilgstosu darbu bojas redze un, visticamak, staja ")
elif a == 2: print(" Mes tiesi saubamies, ka jus sezat pareizi visu darbu pie datora ")
while a>2:
   a=int(input("Meginiet velreiz ievadit atbildi "))
while a<1:
      a=int(input("Meginiet velreiz ievadit atbildi "))   
print(" ")


b=int(input( " Vai majas apmaciba ir kaut kada veida ietekmejusi jusu veselibu?   "))
if b == 1: print(" Patiesam, jo pec macibu jums rodas nogurums un jau negribas nodarboties ar sportu, lai uzturetu savu veselibu ")
elif b == 2: print(" Mes loti saubamies, ka Jus ieverojat visus noteikumus, stradajot pie datora ")
while b>2:
   b=int(input("Meginiet velreiz ievadit atbildi "))
while b<1:
      b=int(input("Meginiet velreiz ievadit atbildi "))   
print(" ")

print(" Izvelieties sev piemerotako atbilde")
print("1. +2 stundas")
print("2. +4 stundas")
print("3. Es visu dienu sezu pie datora, veicot tikai isus partraukumus")
c=int(input( " Cik daudz laika jus pavadat pie datora, neskaitot tieğsaistes stundas? "))
if c == 1: print(" Viss nav tik slikti, jo videji no skolena prasa 2 stundas par majas darbu izpildi ")
elif c == 2: print(" Viss nav tik bedigi, tomer ir vairak verts veltit laiku saviem milijiem un savai veselibai ")
elif c == 3: print(" Visticamak, driz Jums saksies muskulu un kaulu degradacija, paradîsies hronisks stress un nogurums ")
while c>3:
   c=int(input("Meginiet velreiz ievadit atbildi "))
while c<1:
      c=int(input("Meginiet velreiz ievadit atbildi "))   
print(" ")


print(" Izvelieties sev piemerotako atbilde")
print("1. spelu un izklaides")
print("2. lai mekletu kadu informaciju, kas interese mani")
print("3. Jums nav zel sevi un es stradaju brîvaja laika ")
d=int(input( " Par ko jus visbizak izmantojat savu datoru, brivaja laika? "))
if d == 1: print(" Tas ir labi, jo spele viens no labakajiem relaksacijas veidiem. ")
elif d == 2: print(" Tas ir labi, jo jebkurai informacijai ir cena, un noderîga informacija ir nenovertejama.  ")
elif d == 3: print(" Nozelojiet sevi, jo tad var iestaties neatgriezeniskas sekas jusu veselibai ")
while d>3:
   d=int(input("Meginiet velreiz ievadit atbildi "))
while d<1:
      d=int(input("Meginiet velreiz ievadit atbildi "))   
print(" ")


e=int(input( " Vai Jus velaties sanemt daudzus visparigus ieteikumus, lai mazinatu kaitijumu Jusu veselibai?  "))
if e == 1: print("1. Veikt periodiskus partraukumus "); print("2. Pareizi sakartojiet savu darba vietu "); print("3. Centieties saglabat pareizu staju"); print("4. Veiciet treninus")
elif e == 2: print(" Programma ir pabeigusi savu darbu ")
while e>2:
   e=int(input("Meginiet velreiz ievadit atbildi "))
while e<1:
      e=int(input("Meginiet velreiz ievadit atbildi "))   
print(" ")

print( " Paldies par iesniegtajam atbildem! ")