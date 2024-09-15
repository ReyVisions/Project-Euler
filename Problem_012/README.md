Methode naive:
On verifie tous les diviseurs entre 1 et max (mais plus long)

Methode optimisee:
Utiliser le critere racine de n, calculer les diviseurs entre 1 et racine de n
CEPENDANT, ajouter les diviseurs deux par deux.
Car, par exemple pour 100: 2 est diviseurs, donc on a 50 aussi; 4 est diviseur, on a 25 aussi etc... racine de 100 = 10 est la limite. 

Preuve:
e et e' >0
Prouvons que si 10-e est facteur, 10 + e' est son deuxieme facteur. Par l'absurde, si le deuxieme facteur est <10: (10-e)(10-e')=100-10e-10e'+ee'=100-(10-e')e-10e'=100-(10-e)e'-10e. 
(10-e)10=100-10e<100 donc si le premier facteur est plus petit que racine de n, le deuxieme est necessairement plus grand que 10.