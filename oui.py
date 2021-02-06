import random
import os
"""
Définition de la convention :
1 : pion blanc
2 : Tour blanche
3 : Cavalier blanc
4 : Fou blanc
5 : Dame blanche
6 : Roi blanc
7 : pion noir
8 : Tour noir
9 : Cavalier noir
10 : Fou noir
11 : Dame noire
12 : Roi noir
"""

def info_case(x,y,l):
    if(l[x][y] == 0):
        return "vide"
    if(l[x][y] < 7):
        return "blanc"
    if(l[x][y] >= 7):
        return "noir"
def posit():
    """
    Fonction qui initialise le jeu avec la convention définie précedemment.
    """
    l = [[8,9,10,11,12,10,9,8],
         [7,7,7,7,7,7,7,7],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [2,3,4,5,6,4,3,2]]
    return l

camp_noir = [{"type":"p","pos":"a7","coups":["a6","a5"]},
             {"type":"p","pos":"b7","coups":["b6","b5"]},
             {"type":"p","pos":"c7","coups":["c6","c5"]},
             {"type":"p","pos":"d7","coups":["d6","d5"]},
             {"type":"p","pos":"e7","coups":["e6","e5"]},
             {"type":"p","pos":"f7","coups":["f6","f5"]},
             {"type":"p","pos":"g7","coups":["g6","g5"]},
             {"type":"p","pos":"h7","coups":["h6","h5"]},
             {"type":"t","pos":"a8","coups":[]},
             {"type":"t","pos":"h8","coups":[]},
             {"type":"c","pos":"b8","coups":[]},
             {"type":"c","pos":"g8","coups":[]},
             {"type":"f","pos":"c8","coups":[]},
             {"type":"f","pos":"f8","coups":[]},
             {"type":"d","pos":"d8","coups":[]},
             {"type":"r","pos":"e8","coups":[]}]

camp_blanc = [{"type":"p","pos":"a2","coups":["a3","a4"]},
             {"type":"p","pos":"b2","coups":["b3","b4"]},
             {"type":"p","pos":"c2","coups":["c3","c4"]},
             {"type":"p","pos":"d2","coups":["d3","d4"]},
             {"type":"p","pos":"e2","coups":["e3","e4"]},
             {"type":"p","pos":"f2","coups":["f3","f4"]},
             {"type":"p","pos":"g2","coups":["g3","g4"]},
             {"type":"p","pos":"h2","coups":["h3","h4"]},
             {"type":"t","pos":"a1","coups":[]},
             {"type":"t","pos":"h1","coups":[]},
             {"type":"c","pos":"b1","coups":[]},
             {"type":"c","pos":"g1","coups":[]},
             {"type":"f","pos":"c1","coups":[]},
             {"type":"f","pos":"f1","coups":[]},
             {"type":"d","pos":"d1","coups":[]},
             {"type":"r","pos":"e1","coups":[]}]
# ex de chaine : "rg1 f2 g2 h2"
def coo_to_mat(s):
    a = 8-int(s[1])
    b = ord(s[0].lower()) - 97
    return (a,b)

def mat_to_coo(x,y):
    nb = 8-x
    l = chr(97+y)
    return (str(l) + str(nb))

def saisie_pieces():
    res=[[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
    print("Veuillez saisir la combinaison pour les pions blancs")
    a = input()
    if(len(a)>=2):
        tmp = a.split()
        for i in tmp:
            val = 1
            if(len(i) >= 3):
                if(i[0]=='r'):
                    val = 6
                elif(i[0]=='d'):
                    val = 5
                elif(i[0]=='c'):
                    val = 3
                elif(i[0]=='t'):
                    val = 2
                elif(i[0]=='f'):
                    val = 4
                i = i[1:]
            (a,b) = coo_to_mat(i)
            res[a][b] = val
    print("Veuillez saisir la combinaison pour les pions noirs")
    a = input()
    if(len(a)>=2):
        tmp = a.split()
        for i in tmp:
            val = 7
            if(len(i) >= 3):
                if(i[0]=='r'):
                    val = 12
                elif(i[0]=='d'):
                    val = 11
                elif(i[0]=='c'):
                    val = 9
                elif(i[0]=='t'):
                    val = 8
                elif(i[0]=='f'):
                    val = 10
                i = i[1:]
            (a,b) = coo_to_mat(i)
            res[a][b] = val
    print(res)
"""
Définition de la convention :
1 : pion blanc
2 : Tour blanche
3 : Cavalier blanc
4 : Fou blanc
5 : Dame blanche
6 : Roi blanc
7 : pion noir
8 : Tour noir
9 : Cavalier noir
10 : Fou noir
11 : Dame noire
12 : Roi noir
"""
def affiche(l):
    nbligne = 8
    for i in l:
        print("  +---+---+---+---+---+---+---+---+")
        print(nbligne,end=" ")  
        nbligne -= 1
        for e in i:
            if(e == 0):
                print("|"," ",end=" ")
            if(e == 7):
                print("|",chr(0x2659),end=" ")
            if(e == 8):
                print("|",chr(0x2656),end=" ")
            if(e == 9):
                print("|",chr(0x2658),end=" " )
            if(e == 10):
                print("|",chr(0x2657),end=" ")
            if(e == 11):
                print("|",chr(0x2655),end=" ")
            if(e == 12):
                print("|",chr(0x2654),end=" ")
            if(e == 1):
                print("|",chr(0x265F),end=" ")
            if(e == 2):
                print("|",chr(0x265C),end=" ")
            if(e == 3):
                print("|",chr(0x265E),end=" ")
            if(e == 4):
                print("|",chr(0x265D),end=" ")
            if(e == 5):
                print("|",chr(0x265B),end=" ")
            if(e == 6):
                print("|",chr(0x265A),end=" ")
        print("|")
    print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H ")
    
def affiche_bside(l):
    nbligne = 1
    for i in range(7,-1,-1):
        print("  +---+---+---+---+---+---+---+---+")
        print(nbligne,end=" ")
        nbligne += 1
        for e in range(7,-1,-1):
            if(l[i][e] == 0):
                print("|"," ",end=" ")
            if(l[i][e] == 7):
                print("|",chr(0x2659),end=" ")
            if(l[i][e] == 8):
                print("|",chr(0x2656),end=" ")
            if(l[i][e] == 9):
                print("|",chr(0x2658),end=" " )
            if(l[i][e] == 10):
                print("|",chr(0x2657),end=" ")
            if(l[i][e] == 11):
                print("|",chr(0x2655),end=" ")
            if(l[i][e] == 12):
                print("|",chr(0x2654),end=" ")
            if(l[i][e] == 1):
                print("|",chr(0x265F),end=" ")
            if(l[i][e] == 2):
                print("|",chr(0x265C),end=" ")
            if(l[i][e] == 3):
                print("|",chr(0x265E),end=" ")
            if(l[i][e] == 4):
                print("|",chr(0x265D),end=" ")
            if(l[i][e] == 5):
                print("|",chr(0x265B),end=" ")
            if(l[i][e] == 6):
                print("|",chr(0x265A),end=" ")
        print("|")
    print("  +---+---+---+---+---+---+---+---+")
    print("    H   G   F   E   D   C   B   A ")

#te =    [[0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0]]
#affiche_bside(posit())
#print("\n")
#affiche(posit())
def liste_coups_roi(x,y,l):
    res = []
    idroi = l[x][y]
    if((7>=x-1>=0 and 7>=y-1>=0) and (l[x-1][y-1] == 0 or 18 >= l[x-1][y-1] + idroi >= 13)):
        res.append(mat_to_coo(x-1,y-1))
    if((7>=x-1>=0) and (l[x-1][y] == 0 or 18 >= l[x-1][y] + idroi >= 13)):
        res.append(mat_to_coo(x-1,y))
    if((7>=x-1>=0 and 7>=y+1>=0) and (l[x-1][y+1] == 0 or 18 >= l[x-1][y+1] + idroi >= 13)):
        res.append(mat_to_coo(x-1,y+1))
    if((7>=y-1>=0) and (l[x][y-1] == 0 or 18 >= l[x][y-1] + idroi >= 13)):
        res.append(mat_to_coo(x,y-1))
    if((7>=y+1>=0) and (l[x][y+1] == 0 or 18 >= l[x][y+1] + idroi >= 13)):
        res.append(mat_to_coo(x,y+1))
    if((7>=x+1>=0 and 7>=y-1>=0) and (l[x+1][y-1] == 0 or 18 >= l[x+1][y-1] + idroi >= 13)):
        res.append(mat_to_coo(x+1,y-1))
    if((7>=x+1>=0) and (l[x+1][y] == 0 or 18 >= l[x+1][y] + idroi >= 13)):
        res.append(mat_to_coo(x+1,y))
    if((7>=x+1>=0 and 7>=y+1>=0) and (l[x+1][y+1] == 0 or 18 >= l[x+1][y+1] + idroi >= 13)):
        res.append(mat_to_coo(x+1,y+1))
    return res

def liste_coups_fou(x,y,l):
    res = []
    idfou = l[x][y]
    tmpx,tmpy = x+1,y+1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(16>=l[tmpx][tmpy] + idfou>=11):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
        tmpy+=1
    tmpx,tmpy = x-1,y+1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(16>=l[tmpx][tmpy] + idfou>=11):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
        tmpy+=1
    tmpx,tmpy = x+1,y-1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(16>=l[tmpx][tmpy] + idfou>=11):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
        tmpy-=1
    tmpx,tmpy = x-1,y-1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(16>=l[tmpx][tmpy] + idfou>=11):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
        tmpy-=1
    return res

def liste_coups_tour(x,y,l):
    res = []
    idtour = l[x][y]
    tmpx,tmpy = x+1,y
    while(7>=tmpx>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(14>=l[tmpx][tmpy] + idtour>=9):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
    tmpx,tmpy = x-1,y
    while(7>=tmpx>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(14>=l[tmpx][tmpy] + idtour>=9):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
    tmpx,tmpy = x,y-1
    while(7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(14>=l[tmpx][tmpy] + idtour>=9):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpy-=1
    tmpx,tmpy = x,y+1
    while(7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(14>=l[tmpx][tmpy] + idtour>=9):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpy+=1
    return res

def liste_coups_dame(x,y,l):
    res = []
    iddame = l[x][y]
    tmpx,tmpy = x+1,y+1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
        tmpy+=1
    tmpx,tmpy = x-1,y+1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
        tmpy+=1
    tmpx,tmpy = x+1,y-1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
        tmpy-=1
    tmpx,tmpy = x-1,y-1
    while(7>=tmpx>=0 and 7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
        tmpy-=1
    tmpx,tmpy = x+1,y
    while(7>=tmpx>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx+=1
    tmpx,tmpy = x-1,y
    while(7>=tmpx>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpx-=1
    tmpx,tmpy = x,y-1
    while(7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpy-=1
    tmpx,tmpy = x,y+1
    while(7>=tmpy>=0):
        if(l[tmpx][tmpy] == 0):
            res.append(mat_to_coo(tmpx,tmpy))
        elif(17>=l[tmpx][tmpy] + iddame>=12):
            res.append(mat_to_coo(tmpx,tmpy))
            break
        else:
            break
        tmpy+=1
    return res

def liste_coups_cavalier(x,y,l):
    res = []
    idcav = l[x][y]
    if((7>=x-2>=0 and 7>=y-1>=0) and (l[x-2][y-1] == 0 or 15 >= l[x-2][y-1] + idcav >= 10)):
        res.append(mat_to_coo(x-2,y-1))
    if((7>=x-2>=0 and 7>=y+1>=0) and (l[x-2][y+1] == 0 or 15 >= l[x-2][y+1] + idcav >= 10)):
        res.append(mat_to_coo(x-2,y+1))
    if((7>=x-1>=0 and 7>=y+2>=0) and (l[x-1][y+2] == 0 or 15 >= l[x-1][y+2] + idcav >= 10)):
        res.append(mat_to_coo(x-1,y+2))
    if((7>=x+1>=0 and 7>=y+2>=0) and (l[x+1][y+2] == 0 or 15 >= l[x+1][y+2] + idcav >= 10)):
        res.append(mat_to_coo(x+1,y+2))
    if((7>=x+2>=0 and 7>=y+1>=0) and (l[x+2][y+1] == 0 or 15 >= l[x+2][y+1] + idcav >= 10)):
        res.append(mat_to_coo(x+2,y+1))
    if((7>=x+2>=0 and 7>=y-1>=0) and (l[x+2][y-1] == 0 or 15 >= l[x+2][y-1] + idcav >= 10)):
        res.append(mat_to_coo(x+2,y-1))
    if((7>=x+1>=0 and 7>=y-2>=0) and (l[x+1][y-2] == 0 or 15 >= l[x+1][y-2] + idcav >= 10)):
        res.append(mat_to_coo(x+1,y-2))
    if((7>=x-1>=0 and 7>=y-2>=0) and (l[x-1][y-2] == 0 or 15 >= l[x-1][y-2] + idcav >= 10)):
        res.append(mat_to_coo(x-1,y-2))
    return res

def liste_coups_pion(x,y,l):
    res = []
    idpion = l[x][y]
    if(idpion == 7):
        if(x == 1):
            res.append(mat_to_coo((x+2),y))
        if(x+1 <=7 and l[x+1][y] == 0):
            res.append(mat_to_coo(x+1,y))
        if(x+1 <=7 and y+1<=7 and l[x+1][y+1] <= 6):
            res.append(mat_to_coo(x+1,y+1))
        if(x+1 <=7 and 0 <= y-1 <=7 and l[x+1][y-1] <= 6):
            res.append(mat_to_coo(x+1,y-1))
    else:
        if(x == 6):
            res.append(mat_to_coo((x-2),y))
        if(0 <= x-1 <=7 and l[x-1][y] == 0):
            res.append(mat_to_coo(x-1,y))
        if(0 <= x-1 <=7 and y+1<=7 and l[x-1][y+1] >= 6):
            res.append(mat_to_coo(x-1,y+1))
        if(0 <= x-1 <=7 and 0 <= y-1 <=7 and l[x-1][y-1] >= 6):
            res.append(mat_to_coo(x-1,y-1))
    return res

def actu(l):
    for i in range(8):
        for e in range(8):
            if(l[i][e] == 1):
                liste_coup = liste_coups_pion(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 2):
                liste_coup = liste_coups_tour(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 3):
                liste_coup = liste_coups_cavalier(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 4):
                liste_coup = liste_coups_fou(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 5):
                liste_coup = liste_coups_dame(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 6):
                liste_coup = liste_coups_roi(i,e,l)
                for elt in camp_blanc:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 7):
                liste_coup = liste_coups_pion(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 8):
                liste_coup = liste_coups_tour(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 9):
                liste_coup = liste_coups_cavalier(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 10):
                liste_coup = liste_coups_fou(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 11):
                liste_coup = liste_coups_dame(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup
            elif(l[i][e] == 12):
                liste_coup = liste_coups_roi(i,e,l)
                for elt in camp_noir:
                    if(elt["pos"] == mat_to_coo(i,e)):
                        elt["coups"] = liste_coup

def is_correct(coup):
    tmp0 = ord(coup[0].lower())
    tmp1 = ord(coup[1])
    tmp2 = ord(coup[2].lower())
    tmp3 = ord(coup[3])
    return(104>=tmp0>=97 and 104>=tmp2>=97 and 56>=tmp1>=49 and 56>=tmp3>=49)
    
def is_valid(caseini,coup,camp):
    for i in camp:
        if i["pos"]==caseini:
            return coup in i["coups"]
def coup_ordi(camp):
    i = random.randrange(0,16)
    while(len(camp[i]["coups"]) == 0):
        i = random.randrange(0,16)
    tmp = random.randrange(0,len(camp[i]["coups"]))
    return(camp[i]["pos"]+camp[i]["coups"][tmp])
    
def pionintodame(plateau):
    for i in range(8):
        if plateau[0][i] == 1:
            plateau[0][i] = 5
            break
    for i in range(8):
        if plateau[7][i] == 7:
            plateau[7][i] = 11
            break
    return plateau

def affiche_listecoups(camp):
    for i in camp:
        if(len(i["coups"]) != 0):
            print("pos : " +i["pos"])
            print("coups : "+str(i["coups"]))

clear = lambda: os.system("clear")

"""
Définition de la convention :
1 : pion blanc
2 : Tour blanche
3 : Cavalier blanc
4 : Fou blanc
5 : Dame blanche
6 : Roi blanc
7 : pion noir
8 : Tour noir
9 : Cavalier noir
10 : Fou noir
11 : Dame noire
12 : Roi noir
"""

#####################################################################################
#####################################################################################
##############################PROGRAMME PRINCIPAL####################################
#####################################################################################
#####################################################################################
print("Quelle couleur souhaitez-vous ? B/N")
clr = input()
while(clr.lower() != 'b' and clr.lower() != 'n'):
    print("Veuillez saisir B ou N pour choisir votre couleur")
    clr = input()
if(clr.lower() == 'b'):
    plateau = posit()
    oui = True
    while(camp_noir[-1]["pos"] != "" or camp_blanc[-1]["pos"] != "" and oui):
        affiche(plateau)
        if(camp_noir[-1]["pos"] == "" or camp_blanc[-1]["pos"] == ""):
            break
        print("Veuillez entrer un coup à jouer (ou \"help\" pour connaitre le format)")
        print("Si vous voulez connaitre la liste des coups disponibles tapez \"liste\"")
        coup_utilisateur = input()
        if(coup_utilisateur=="q"):
            oui = False
            print("Partie interrompue")
            break
        if(coup_utilisateur=="help"):
            print("Le format est le suivant : case initiale case d'arrivée Ex : e2e4")
            print("Veuillez entrer votre coup")
            coup_utilisateur=input()
        if(coup_utilisateur=="liste"):
            print("Voici la liste des coups disponibles avec pos la position initiale")
            affiche_listecoups(camp_blanc)
            print("Veuillez entrer votre coup")
            coup_utilisateur=input()
        while(not(is_correct(coup_utilisateur))):
            if(coup_utilisateur=="q"):
                oui = False
                print("Partie interrompue")
                break
            print("Vous avez entré "+coup_utilisateur+" qui est un coup incorrect.")
            print("Merci de respecter le format suivant : case initiale case d'arrivée Ex : e2e4")
            coup_utilisateur = input()
        caseini = coup_utilisateur[:2]
        casefin = coup_utilisateur[2:]
        while(not(is_valid(caseini,casefin,camp_blanc))):
            print("Le coup que vous avez entré n'est pas légal, merci de réessayer")
            if(coup_utilisateur=="q"):
                oui = False
                print("Partie interrompue")
                break
            coup_utilisateur=input()
            caseini = coup_utilisateur[:2]
            casefin = coup_utilisateur[2:]  
        print("vous avez entré un coup valide et légal !")
        caseini = coup_utilisateur[:2]
        casefin = coup_utilisateur[2:]
        x,y = coo_to_mat(casefin)
        tmp1,tmp2 = coo_to_mat(caseini)
        idpiece = plateau[tmp1][tmp2]
        if(plateau[x][y] == 0):
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_blanc:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
        else:
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_blanc:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
            for i in camp_noir:
                if i["pos"] == casefin:
                    i["pos"] = ""
        coupord = coup_ordi(camp_noir)
        clear()
        print("Le coup entré par l'ordinateur est le suivant : "+coupord)
        caseini = coupord[:2]
        casefin = coupord[2:]
        x,y = coo_to_mat(casefin)
        tmp1,tmp2 = coo_to_mat(caseini)
        idpiece = plateau[tmp1][tmp2]
        if(plateau[x][y] == 0):
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_noir:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
        else:
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_noir:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
            for i in camp_blanc:
                if i["pos"] == casefin:
                    i["pos"] = ""
        plateau = pionintodame(plateau)
        actu(plateau)

if(clr.lower() == 'n'):
    plateau = posit()
    oui = True
    while(camp_noir[-1]["pos"] != "" or camp_blanc[-1]["pos"] != "" and oui):
        #affiche_listecoups(camp_noir)
        if(camp_noir[-1]["pos"] == "" or camp_blanc[-1]["pos"] == ""):
            break
        coupord = coup_ordi(camp_blanc)
        print("Le coup entré par l'ordinateur est le suivant : "+coupord)
        caseini = coupord[:2]
        casefin = coupord[2:]
        x,y = coo_to_mat(casefin)
        tmp1,tmp2 = coo_to_mat(caseini)
        idpiece = plateau[tmp1][tmp2]
        if(plateau[x][y] == 0):
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_blanc:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
        else:
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_blanc:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
            for i in camp_noir:
                if i["pos"] == casefin:
                    i["pos"] = ""
        clear()
        affiche_bside(plateau)
        affiche_listecoups(camp_noir)
        print("Veuillez entrer un coup à jouer (ou taper help pour connaitre le format)")
        print("Si vous voulez connaitre la liste des coups disponibles tapez \"liste\"")
        coup_utilisateur = input()
        if(coup_utilisateur=="q"):
            oui = False
            print("Partie interrompue")
            break
        if(coup_utilisateur=="help"):
            print("Le format est le suivant : case initiale case d'arrivée Ex : e2e4")
            print("Veuillez entrer votre coup")
            coup_utilisateur=input()
        if(coup_utilisateur=="liste"):
            print("Voici la liste des coups disponibles avec pos la position initiale")
            affiche_listecoups(camp_noir)
            print("Veuillez entrer votre coup")
        while(not(is_correct(coup_utilisateur))):
            if(coup_utilisateur=="q"):
                oui = False
                print("Partie interrompue")
                break
            print("Vous avez entré "+coup_utilisateur+" qui est un coup incorrect.")
            print("Merci de respecter le format suivant : case initiale case d'arrivée Ex : e2e4")
            coup_utilisateur = input()
        caseini = coup_utilisateur[:2]
        casefin = coup_utilisateur[2:]
        while(not(is_valid(caseini,casefin,camp_noir))):
            print("Le coup que vous avez entré n'est pas légal, merci de réessayer")
            if(coup_utilisateur=="q"):
                oui = False
                print("Partie interrompue")
                break
            coup_utilisateur=input()
            caseini = coup_utilisateur[:2]
            casefin = coup_utilisateur[2:]  
        print("vous avez entré un coup valide et légal !")
        caseini = coup_utilisateur[:2]
        casefin = coup_utilisateur[2:]
        x,y = coo_to_mat(casefin)
        tmp1,tmp2 = coo_to_mat(caseini)
        idpiece = plateau[tmp1][tmp2]
        if(plateau[x][y] == 0):
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_noir:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
        else:
            plateau[x][y] = idpiece
            plateau[tmp1][tmp2] = 0
            for i in camp_noir:
                if i["pos"] == caseini:
                    i["pos"] = casefin
                    break
            for i in camp_blanc:
                if i["pos"] == casefin:
                    i["pos"] = ""
        clear()
        plateau = pionintodame(plateau)
        actu(plateau)




if(camp_noir[-1]["pos"] == ""):
    print("Le camp blanc est gagnant !")

if(camp_blanc[-1]["pos"] == ""):
    print("Le camp blanc est gagnant !")

print("Merci d'avoir joué !")















