import numpy
import math
from numpy import matrix
from numpy import linalg

''' Alle Funktionen, bei denen nichts anderes extra angegeben ist, wurden von der Verfasserin verfasst'''

## Hilfsfunktionen

'''Die Funktion zum Finden der Determinanten stammt von: https://github.com/mrtoc06/matrix_inverse_determinant/blob/main/determinant.py entnommen (am 05.06.2021)'''
# Ueberpruefen, ob die angegebene Matrix invertierbar ist
def matrix_invertierbar(matrix_f):
    
    # Defining nXn matrix size as N
    N = len(matrix_f)
    # Making lower triangle zero
    for row in range(N):
        for c in range(N-row-1):
            if A[row][row] != 0:
                ratio = - A[row+c+1][row] / A[row][row]
                for col in range(N):
                    A[row+c+1][col] += A[row][col]*ratio
            else:
                temp = A[row]
                A[row] = A[row+1]
                A[row+1] = temp
    determinante = 1
    for i in range(N):
        determinante *= A[i][i]
    
    determinante = determinante % 97
    
    if determinante > 0 or determinante <0:
        return determinante
    
    else: 
        print("\n\n\n\n\n============================================================")
        print("Es tut mir leid, da diese Matrix nicht invertierbar ist, kann Ihr Text damit nicht bearbeitet werden.")

'''Die drei Funktionen zum Invertieren der Mtrix in mod 97 stammen von https://stackoverflow.com/questions/4287721/easiest-way-to-perform-modular-matrix-inversion-with-python und wurden am 05.06.2021 entnommen.'''
# Die Matrix invertieren, falls die Inverse der angegebenen Matrix benötigt wird
def invertieren(matrix_f):       # invertiert matrix_f, falls möglich
  n=len(matrix_f)
  A=matrix(matrix_f)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%97
      matrix_r = (modInv(int(round(linalg.det(A))),97)*adj)%97
  return matrix_r

def modInv(a, p):          # findet Inverse von a mod p, falls existent
  for i in range(1,97):
    if (i*a)%97==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(97))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor
    
# Die Zeichen des Textes in Zahlen umwandeln, damit die Rechnungen durchgeführt werden können
def text_nach_zahl(text_f):
    
    text_zahl_f = []
    
    for zeichen in text_f:
        zahl = ord(zeichen) - 31
        text_zahl_f.append(zahl)
        
    return text_zahl_f

# Den Text aus Zahlen in Blöcke/ Vektoren aufteilen, um die Rechnungen durchführen zu können
def bloecke_bilden(text_zahl_f):

    i = 0
    bloecke = []
    zahl = []
    Dimension = len[matrix_f]
    
    for zeichen in text_zahl_f:
        
        if (i >= Dimension):
            
            bloecke.append(zahl)
            zahl = [];
            i = 0
            
        i += 1
        zahl.append(zeichen)
        
    if (len(zahl) > 0):
        
        if (len(zahl) != Dimension):
            
            for ii in range(0,n-len(zahl)):
                
                zahl.append(0)
                
        bloecke.append(zahl)
    
    return bloecke
    
# Multiplikation von Matrix und Vektor
def matrix_mult(block, matrix_r):
    
    block_1 = []
    n = -1
    
    for zeile in matrix_r:
        
        n = n + 1
        m = 0
        zahl = 0
        
        for wert in matrix_r[n]:
            
            zahl = zahl + block[m] * matrix_r[n][m]
            m = m + 1
            
        block_1.append(zahl)
        
    return block_1
    
# Die Zahlen der multiplizierten Vektoren mod 97 rechnen
def vektor_mod(block_1):
    
    block_2 = []
    
    for zeichen in block_1:
        
        zahl = zeichen % 97
        block_2.append(zahl)
    
    return block_2

# Zusammensetzung der Rechnungen, um den Text zu ent- oder verschlüsseln
def bloecke_ver_und_entschluesseln(bloecke, matrix_r):
    
    for block in bloecke:
        
        bloecke_1 = matrix_mult(block, matrix_r)
        
        for block_1 in bloecke_1:
        
            bloecke_2 = vektor_mod(block_1, mod_zahl)
    
    return bloecke_2
    
# Die Blöcke/Vektoren wieder zu einem ganzen zusammenfügen
def bloecke_zusammenfuegen(bloecke_2):

    text_zahl_r = []

    for block in bloecke_2:
        
        for zeichen in block:
        
            text_zahl_r.append(zeichen)
    
    return text_zahl_r
    
# Die Zahlen zurück in Zeichen umwaneln, damit wieder ein Text rauskommt
def zahl_nach_text(text_zahl_r):
    
    text_r = []
    
    for zeichen in text_zahl_r:
        
        zahl = zeichen + 31
        buchstabe = chr(zahl)
        text_r.append(buchstabe)
        text_2 = "".join(text_r)
        
    return text_2
    
## Benutzerführung

def verschluesseln():
    
    while True:
        print("\n\n\n\n\n============================================================")
        print("Sie haben Text verschlüsseln gewählt, welche Matrix haben Sie gegeben?")
        verfahren_1 = input("1: Entschlüsselungsmatrix     2: Verschlüsselungsmatrix    (Keine Eingabe: Ende)")
        
        #Entschlüsselungsmatrix
        if verfahren_1 == "1":
            print("\n\n\n\n\n============================================================")
            matrix_f = ("Geben Sie bitte ihre Matrix an wie folgt: ((zeile 1 wert 1, zeile 1 wert 2, zeile 1 wert n), (zeile 2 wert 1, zeile 2 wert 2, zeile 2 wert n), (zeile n wert 1, zeile 1 wert 2, zeile n wert )).")
            print("\n\n\n\n\n============================================================")
            matrix_f = input("Geben Sie bitte Ihre Matrix ein.")
            text_f = input("Geben Sie bitte Ihren Klartext ein.")
            
            Determinante = invertieren(matrix_f)
            matrix_r = matrix_invertierbar(matrix_f)
            text_zahl_f = text_nach_zahl(text_f)
            bloecke = bloecke_bilden(text_zahl_f)
            bloecke_2 = bloecke_ver_und_entschluesseln(bloecke, matrix_r)
            text_zahl_r = bloecke_zusammenfuegen(bloecke_2)
            text_2 = zahl_nach_text(text_zahl_r)
            
            print("\n============================================================\n")
            print("Das ist der chiffrierte Text:\n", text_2)
            break
            
        #Verschlüsselungsmatrix
        elif verfahren_1 == "2":
            print("\n\n\n\n\n============================================================")
            matrix_f = ("Geben Sie bitte ihre Matrix an wie folgt: [[zeile 1 wert 1, zeile 1 wert 2, zeile 1 wert n], [zeile 2 wert 1, zeile 2 wert 2, zeile 2 wert n], [zeile n wert 1, zeile 1 wert 2, zeile n wert n ]].")
            print("\n\n\n\n\n============================================================")
            matrix_f = input("Geben Sie bitte Ihre Matrix ein.")
            text_f = input("Geben Sie bitte Ihren Klartext ein.")
            
            Determinante = invertieren(matrix_f)
            matrix_r = matrix_f
            text_zahl_f = text_nach_zahl(text_f)
            bloecke = bloecke_bilden(text_zahl_f)
            bloecke_2 = bloecke_ver_und_entschluesseln(bloecke, matrix_r)
            text_zahl_r = bloecke_zusammenfuegen(bloecke_2)
            text_2 = zahl_nach_text(text_zahl_r)
            
            print("\n============================================================\n")
            print("Das ist der chiffrierte Text:\n", text_2)
            
        #abbrechen
        elif len(verfahren_1) == "0":
            break

def entschluesseln():
    
    while True:
        print("\n\n\n\n\n============================================================")
        print("Sie haben Text entschlüsseln gewählt, welche Matrix haben Sie gegeben?")
        verfahren_1 = input("1: Entschlüsselungsmatrix     2: Verschlüsselungsmatrix    (Keine Eingabe: Ende)")
        
        #Entschlüsselungsmatrix
        if verfahren_1 == "1":
            print("\n\n\n\n\n============================================================")
            matrix_f = ("Geben Sie bitte ihre Matrix an wie folgt: ((zeile 1 wert 1, zeile 1 wert 2, zeile 1 wert n), (zeile 2 wert 1, zeile 2 wert 2, zeile 2 wert n), (zeile n wert 1, zeile 1 wert 2, zeile n wert )).")
            print("\n\n\n\n\n============================================================")
            matrix_f = input("Geben Sie bitte Ihre Matrix ein.")
            text_f = input("Geben Sie bitte Ihr Chiffrat ein.")
            
            Determinante = invertieren(matrix_f)
            matrix_r = matrix_f
            text_zahl_f = text_nach_zahl(text_f)
            bloecke = bloecke_bilden(text_zahl_f)
            bloecke_2 = bloecke_ver_und_entschluesseln(bloecke, matrix_r)
            text_zahl_r = bloecke_zusammenfuegen(bloecke_2)
            text_2 = zahl_nach_text(text_zahl_r)
            
            print("\n============================================================\n")
            print("Das ist der dechiffrierte Text:\n", text_2)
            break
            
        #Verschlüsselungsmatrix
        elif verfahren_1 == "2":
            print("\n\n\n\n\n============================================================")
            matrix_f = ("Geben Sie bitte ihre Matrix an wie folgt: ((zeile 1 wert 1, zeile 1 wert 2, zeile 1 wert n), (zeile 2 wert 1, zeile 2 wert 2, zeile 2 wert n), (zeile n wert 1, zeile 1 wert 2, zeile n wert )).")
            print("\n\n\n\n\n============================================================")
            matrix_f = input("Geben Sie bitte Ihre Matrix ein.")
            text_f = input("Geben Sie bitte Ihr Chiffrat ein.")
            
            Determinante = invertieren(matrix_f)
            matrix_r = matrix_invertierbar(matrix_f)
            text_zahl_f = text_nach_zahl(text_f)
            bloecke = bloecke_bilden(text_zahl_f)
            bloecke_2 = bloecke_ver_und_entschluesseln(bloecke, matrix_r)
            text_zahl_r = bloecke_zusammenfuegen(bloecke_2)
            text_2 = zahl_nach_text(text_zahl_r)
            
            print("\n============================================================\n")
            print("Das ist der dechiffrierte Text:\n", text_2)
            
        #abbrechen
        elif len(verfahren_1) == "0":
            break

while True:
    print("\n\n\n\n\n============================================================")
    print("Herzlich Willkommen!\n\nHier können Sie Texte mit Hilfe der Hill-Chiffre ent- und verschlüsseln.\n\nWas möchten Sie tun?\n\n")
    verfahren = input("1: Text entschlüsseln     2: Text verschlüsseln    (Keine Eingabe: Ende)")
    if verfahren == "1":
        entschluesseln()
    elif verfahren == "2":
        verschluesseln()
    elif len(verfahren) == 0:
        break