# Approche

Le premier instinct est de vouloir creer l'ensemble des combinaisons possibles, puis de les trier, puis de chercher le 1e6 indice.
C'est tout a fait possible, avec des librairies, mais on peut le faire de facon bien plus elegante.

On peut calculer mathematiquement le nombre de combinaisons possibles, et donc predire, pour chaque chiffre lequel va tomber.

Par exemple, nous savons qu'il y a 10! combinaisons possibles pour le problemes. (10 choix pour le premier chiffre, 9 pour le deuxieme etc..)
Si on fixe le premier chiffre par exemple, on a 9! possibilites, ce qui donne 362880<1000000.

Donc entre 1 et 362800-1, le premier chiffre est 0, puis entre 362800 et 2*9!, et ainsi de suite pour les autres chiffres on peut trouver la combinaison.

Mon algorithme traduit d'abord le chiffre de base 10 en base factorielles pour les 9 premier chiffres. Ici, je trouve 2783915460. Pour chaque chiffre je cherche l'indice dans la liste de chiffre [0,1,2,3,4,5,6,7,8,9]. S'il est pas disponible je prends le suivant.

Ce qui donne le resultat.

La complexite est tres faible, et le temps d'execution est de 10ms.