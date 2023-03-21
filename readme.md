1/ Objectifs du projet

On veut créer un jeu hexapawn contre un ordinateur avec une interface grâce à tkinter

L’hexapawn est jeu sur un échiquier de dimension 3x3 où chaque joueur à 3 pions pouvant se déplacer comme les pions au échec. Le but est pour un joueur est soit de faire progresser un de ses pions à l’extrémité opposé soit d’empêcher l’autre joueur de se déplacer. Le joueur se déplace en 1er.

L’ordinateur apprends de ses erreurs, au fur et à mesure des parties l’ordinateur ne pourra plus perdre.

2/ Découpage du projet

Le projet est découpé en 2 partie :

1. Le code du jeu hexapawn (Mathias) :

`	`-Les déplacements du joueur → playerDisplacement()

`	`-Les déplacements du bot → botDisplacement()

`	`-Vérifier si le bot a gagné → botVictoryTest()

`	`-Vérifier si le J1 a gagné → playerVictoryTest()

`	`-Calculer les déplacements possibles du bot → possibleBotDisplacement()

`	`-Calculer les déplacements possibles du joueur → possiblePlayerDisplacement()

`	`-Supprimer les déplacements interdits du bot par son apprentisage → ai()



1. L’interface sur tkinter (Ouamer) :

`	`-Le menu → menu()

`	`-Afficher le plateau de jeu : → jeu()

`		`-Déplacement des pions


3/ Variables

- blockedBotDisplacementList (liste) → stocker les déplacements interdit du bot au fur et à mesure des parties
- chessboard (liste)  
- score (liste) → score entre le joueur et le bot
- playerDisplacementList(liste) →  liste des déplacements disponible pour le joueur calculer a chaque tour
- botDisplacementList(liste) →  liste des déplacements disponible du bot calculer a chaque tour
- oldBotDisplacementList(liste) → liste des déplacements disponible du bot du tour précépant 
- botChoiceReturn →  déplacements que le bot a choisi pendant ce tour
- playerWin(booléen) → variable pour la victoire du joueur
- botWin(booléen) → variable pour la victoire du bot


4/ Test dans la console

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.001.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.002.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.003.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.004.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.005.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.006.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.007.png)

![](Aspose.Words.9d388596-44dc-4419-a122-286c9f516f97.008.png)

