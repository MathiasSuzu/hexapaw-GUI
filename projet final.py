from tkinter import *
from random import randint
import tkinter.font as font

blackCase='#4a4a4a'
whiteCase='#e3decf'


fenetre= Tk()
fenetre.geometry("800x600")
fenetre.resizable(False,False)

scoreIA=IntVar(fenetre, name='scoreIA')
fenetre.setvar(name='scoreIA', value=0)

varscoreIA=StringVar(fenetre,name="varscoreIA")
fenetre.setvar(name="varscoreIA", value='Score IA: 0')

scoreJ=IntVar(fenetre, name='scoreJ')
fenetre.setvar(name='scoreJ', value=0)

varscoreJ=StringVar(fenetre, name="varscoreJ")
fenetre.setvar(name="varscoreJ", value='Score Joueur: 0')

playerWin = BooleanVar(fenetre, name ="playerWin")
botwin = BooleanVar(fenetre, name ="botwin")

pionBlanc=PhotoImage(file="whitepawn1.gif")
pionNoir=PhotoImage(file="blackpawn1.gif")
vide = PhotoImage(file="void1.gif")


def resetChessboard():
    for i in range(len(chessboard)):
        chessboard.pop()
    chessboard.append([20, 21, 22])
    chessboard.append([0, 0, 0])
    chessboard.append([10, 11, 12])

def affichage():
    if chessboard[0][0] != 0 :
        pawn = chessboard[0][0]
        if pawn//10 == 1 :
            case0.itemconfig(case0Image, image=pionBlanc)
        else:
            case0.itemconfig(case0Image, image=pionNoir)
    else:
        case0.itemconfig(case0Image, image=vide)


    if chessboard[0][1] != 0 :
        pawn = chessboard[0][1]
        if pawn//10 == 1 :
            case1.itemconfig(case1Image, image=pionBlanc)
        else:
            case1.itemconfig(case1Image, image=pionNoir)
    else:
        case1.itemconfig(case1Image, image=vide)

    if chessboard[0][2] != 0 :
        pawn = chessboard[0][2]
        if pawn//10 == 1 :
            case2.itemconfig(case2Image, image=pionBlanc)
        else:
            case2.itemconfig(case2Image, image=pionNoir)
    else:
        case2.itemconfig(case2Image, image=vide)
    
    if chessboard[1][0] != 0 :
        pawn = chessboard[1][0]
        if pawn//10 == 1 :
            case3.itemconfig(case3Image, image=pionBlanc)
        else:
            case3.itemconfig(case3Image, image=pionNoir)
    else:
        case3.itemconfig(case3Image, image=vide)

    if chessboard[1][1] != 0 :
        pawn = chessboard[1][1]
        if pawn//10 == 1 :
            case4.itemconfig(case4Image, image=pionBlanc)
        else:
            case4.itemconfig(case4Image, image=pionNoir)
    else:
        case4.itemconfig(case4Image, image=vide)

    if chessboard[1][2] != 0 :
        pawn = chessboard[1][2]
        if pawn//10 == 1 :
            case5.itemconfig(case5Image, image=pionBlanc)
        else:
            case5.itemconfig(case5Image, image=pionNoir)
    else:
        case5.itemconfig(case5Image, image=vide)
    
    if chessboard[2][0] != 0 :
        pawn = chessboard[2][0]
        if pawn//10 == 1 :
            case6.itemconfig(case6Image, image=pionBlanc)
        else:
            case6.itemconfig(case6Image, image=pionNoir)
    else:
        case6.itemconfig(case6Image, image=vide)

    if chessboard[2][1] != 0 :
        pawn = chessboard[2][1]
        if pawn//10 == 1 :
            case7.itemconfig(case7Image, image=pionBlanc)
        else:
            case7.itemconfig(case7Image, image=pionNoir)
    else:
        case7.itemconfig(case7Image, image=vide)

    if chessboard[2][2] != 0 :
        pawn = chessboard[2][2]
        if pawn//10 == 1 :
            case8.itemconfig(case8Image, image=pionBlanc)
        else:
            case8.itemconfig(case8Image, image=pionNoir)
    else:
        case8.itemconfig(case8Image, image=vide)

def possibleBotDisplacement():
    
    possibleDisplacementList = []

    for column in range(3): #listage des pions noirs qui peuvent se déplacés.
        for k in chessboard[column]:
            if k//10 == 2 :
                line = chessboard[column].index(k)

                local = []
                local.append([column, line, k])
 
                if column+1 < 3 :

                    if line-1 > -1 and chessboard[column+1][line-1]//10 == 1:
                        local.append(-1)

                    if chessboard[column+1][line]//10 == 0:
                        local.append(0)

                    if line+1 < 3 and chessboard[column+1][line+1]//10 == 1:
                        local.append(1)
                    
                    if len(local) != 1:
                        possibleDisplacementList.append(local)
                        
    return possibleDisplacementList

def possiblePlayerDisplacement():
    
    possibleDisplacementList = []

    for column in range(3): #listage des pions noirs qui peuvent se déplacés.
        for k in chessboard[column]:
            if k//10 == 1 :
                line = chessboard[column].index(k)

                local = []
                local.append([column, line, k])
 
                if column-1 >= 0 :

                    if line-1 > -1 and chessboard[column-1][line-1]//10 == 2:
                        local.append(-1)

                    if chessboard[column-1][line]//10 == 0:
                        local.append(0)

                    if line+1 < 3 and chessboard[column-1][line+1]//10 == 2:
                        local.append(1)
                    
                    if len(local) != 1:
                        possibleDisplacementList.append(local)                    
    return possibleDisplacementList

def playerDisplacement(pawn, displacement, playerDisplacementList : list):

    good = False

    for i in range(3):
        if pawn//10 == 1 and displacement >= -1 and displacement <= 1 and  pawn == playerDisplacementList[i][0][2] and displacement in playerDisplacementList[i]:
            line = playerDisplacementList[i][0][0]
            colon = playerDisplacementList[i][0][1]

            good = True
            break
        
    if good == False : 
        return False

    if displacement == 0:
        chessboard[line][colon] = 0
        chessboard[line-1][colon] = pawn
        return True
    
    elif displacement == -1:
        chessboard[line][colon] = 0
        chessboard[line-1][colon-1] = pawn
        return True
    
    elif displacement == 1:
        chessboard[line][colon] = 0
        chessboard[line-1][colon+1] = pawn
        return True

def botDisplacement(botDisplacementList):
    r1 = randint(0, len(botDisplacementList)-1)
    r2 = randint(1, len(botDisplacementList[r1])-1)     

    line = botDisplacementList[r1][0][0]
    colon = botDisplacementList[r1][0][1]
    pawn = botDisplacementList[r1][0][2]
    displacement = botDisplacementList[r1][r2]

    if displacement == 0:
        chessboard[line+1][colon] = pawn

    elif displacement == -1:
        chessboard[line+1][colon-1] = pawn

    elif displacement == 1:
        chessboard[line+1][colon+1] = pawn

    chessboard[line][colon] = 0

    return[r1, r2]

def playerVictoryTest(botDisplacementList):
    if botDisplacementList == [] : return True
    
    for k in chessboard[0]:
        if k//10 == 1:
            return True
    
    return False

def botVictoryTest(playerDisplacementList):
    if playerDisplacementList == [] : return True
    
    for k in chessboard[2]:
        if k//10 == 2:
            return True
    
    return False

def fenetreDeplacement(available):
    fenetre=Tk()

    fenetre.geometry('500x200')

    choice = []
    def setchoice(a):
        choice.append(a)
    
    def getchoice():
        return choice[0]

    def printDroite():
        setchoice(1)
        fenetre.quit()

    def printMilieu():
        setchoice(0)
        fenetre.quit()

    def printGauche():
        setchoice(-1)
        fenetre.quit()

    font1=font.Font(size=10)

    if -1 in available : 
        buttonGauche=Button(fenetre,command=printGauche,text='↖')
        buttonGauche['font']=font1
        buttonGauche.place(x=120,y=100,anchor=N)
    if 0 in available:
        buttonMilieu=Button(fenetre,command=printMilieu,text='↑')
        buttonMilieu['font']=font1
        buttonMilieu.place(x=240,y=100,anchor=N)
    if 1 in available:
        buttonDroite=Button(fenetre,command=printDroite,text='↗')
        buttonDroite['font']=font1
        buttonDroite.place(x=360,y=100,anchor=N)


    fenetre.mainloop()
    fenetre.destroy()
    return getchoice()

def ai(botDisplacementList, blockedBotDisplacementList) :
    for i in blockedBotDisplacementList:
        if i[0] == botDisplacementList:
            r1 = i[1][0]
            r2 = i[1][1]

            del (botDisplacementList[r1]) [r2]

            if len(botDisplacementList[r1]) == 1 :
                del (botDisplacementList) [r1]

    return botDisplacementList

def clickG(event):

    if fenetre.getvar(name='playerWin') :
        fenetre.setvar(name="playerWin", value=False)
        resetChessboard()
        affichage()
        return
    elif fenetre.getvar(name='botwin'):
        fenetre.setvar(name="botwin", value=False)
        resetChessboard()
        affichage()
        return

    numberCase = str(event.widget)[8:]
    if numberCase == "" : numberCase = 1

    numberCase = int(numberCase)-1

    ligne = numberCase//3
    colone = numberCase%3

    if chessboard[ligne][colone]//10 != 1:
        return

    playerDisplacementList = possiblePlayerDisplacement()

    pawn = chessboard[ligne][colone]
    selected = [ligne, colone, pawn]

    available = []

    for i in playerDisplacementList:
        if i[0] == selected:
            available = i.copy()
            available.pop(0)

    playerDisplacement(pawn, fenetreDeplacement(available), playerDisplacementList)
    
    botDisplacementList = possibleBotDisplacement()
    fenetre.setvar(name="playerWin", value=playerVictoryTest(botDisplacementList))
    if fenetre.getvar(name='playerWin') == False:
        botDisplacementList = ai(botDisplacementList, blockedDisplacementList)
        setBotChoice(botDisplacement(botDisplacementList))
        playerDisplacementList = possiblePlayerDisplacement()
        fenetre.setvar(name="botwin", value=botVictoryTest(playerDisplacementList))
        
    else:
        addinBlockedDisplacementList([oldBotDisplacementList.copy(), getBotChoice().copy()])
        fenetre.setvar(name='scoreJ', value=fenetre.getvar(name='scoreJ')+1)
        fenetre.setvar(name='varscoreJ', value=('Score Joueur: ' + str(fenetre.getvar(name='scoreJ'))))

    if fenetre.getvar(name='botwin'):
        fenetre.setvar(name='scoreIA', value=fenetre.getvar(name='scoreIA')+1)
        fenetre.setvar(name='varscoreIA', value=('Score IA: ' + str(fenetre.getvar(name='scoreIA'))))

    setOldDisplacementList(botDisplacementList)
    affichage()

chessboard = [
    [20, 21, 22],
    [0, 0, 0],
    [10, 11, 12]
]

oldBotDisplacementList = []
blockedDisplacementList = []
botChoiceList = []

def getOldDisplacementList():
    return oldBotDisplacementList

def setOldDisplacementList(botDisplacementList):
    for i in range(len(oldBotDisplacementList)):
        oldBotDisplacementList.pop()

    for i in botDisplacementList:
        oldBotDisplacementList.append(i)

def getBlockedDisplacementList():
    return blockedDisplacementList

def addinBlockedDisplacementList(i):
    blockedDisplacementList.append(i)

def getBotChoice():
    return botChoiceList

def setBotChoice(b):
    for i in range(len(botChoiceList)):
        botChoiceList.pop()
    for j in b:
        botChoiceList.append(j)


case0=Canvas(fenetre,width=200,height=200,background=blackCase)
case0Image=case0.create_image(100,100,image=vide)
case0.place(x=0,y=0)
case1=Canvas(fenetre,width=200,height=200,background=whiteCase)
case1Image=case1.create_image(100,100,image=vide)
case1.place(x=200,y=0)
case2=Canvas(fenetre,width=200,height=200,background=blackCase)
case2Image=case2.create_image(100,100,image=vide)
case2.place(x=400,y=0)
case3=Canvas(fenetre,width=200,height=200,background=whiteCase)
case3Image=case3.create_image(100,100,image=vide)
case3.place(x=0,y=200)
case4=Canvas(fenetre,width=200,height=200,background=blackCase)
case4Image=case4.create_image(100,100,image=vide)
case4.place(x=200,y=200)
case5=Canvas(fenetre,width=200,height=200,background=whiteCase)
case5Image=case5.create_image(100,100,image=vide)
case5.place(x=400,y=200)
case6=Canvas(fenetre,width=200,height=200,background=blackCase)
case6Image=case6.create_image(100,100,image=vide)
case6.place(x=0,y=400)
case7=Canvas(fenetre,width=200,height=200,background=whiteCase)
case7Image=case7.create_image(100,100,image=vide)
case7.place(x=200,y=400)
case8=Canvas(fenetre,width=200,height=200,background=blackCase)
case8Image=case8.create_image(100,100,image=vide)
case8.place(x=400,y=400)

affichage()

fenetre.bind_class('Canvas','<Button-1>',clickG)
afficheScoreIA=Label(fenetre,textvariable=varscoreIA).place(x=620,y=0)
afficheScoreJ=Label(fenetre,textvariable=varscoreJ).place(x=620,y=50)

fenetre.mainloop()