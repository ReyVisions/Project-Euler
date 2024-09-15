Il y a deux solutions: Une naive et une optimisee

# NAIVE

On compose le resultat de la fonction collatz jusqu'a obtenir 1.
Fonctionne mais une question se pose: si on repasse par la meme serie de nombre, est ce qu'on peut pas optimiser?

# OPTIMALE

On peut calculer uniquement les nouveaux "chemins" qu'on emprunte, on stocke donc les donnees sous forme de dictionnaire. On stocke en cle n, et en valeurs la taille du chemin pour obtenir 1.
Comment faire?
Pour la valeurs n, s'il n'y a pas de valeur attribuee, on compose par la fonction collatz et on verifie jusqu'a tomber sur une cle dont on a la valeur, ou il suffira d'ajouter sa valeur. Cependant, on peut uniquement ajouter la valeurs avant celle qu'on connait. Puis l'avant derniere et ainsi de suite.

Donc on stocke le chemin inconnu et on s'arrete quand on tombe sur un chemin connu.
Puis on ajoute valeur par valeurs suivant le chemin inverse. A chaque incrementation il suffit de rajouter 1 a la longueur.

Exemple:
n=3
dico={1:1,2:2}
3->10->5->16->8->4->2 qu'on connait.
on stocke [3,10,5,16,8,4] dans une liste, et on met a jour: 4:3, puis 8:4, puis 16:5, puis 5:6, puis 10:7, puis 3:8.
n=4 on a deja le resultat.


Pour le probleme on passe d'un temps de 6.51008 secondes a 0.78538 secondes.