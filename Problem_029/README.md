# 📘 Projet Euler – Problème *28*  

## 📊 Estimation de la difficulté  
👉 **5% – [Très facile / ->>Facile / Moyen / Difficile / Très difficile]**  

---

## 💡 Idée générale  
Facile pour un 5%. On peut se perdre dans la formalisation du problème mais en étudiant le cas on peut faire un programme calculant très facilement pour tous les cas.

---
## 🚀 Stratégies/Indices de résolution  
1. [Indice 1 : Résonner sous forme de récurrence.]  
2. [Indice 2 : Essayer d'exprimer la somme au rang 2k+3 en fonction de 2k+1 (car la recurrence est seulement sur les impairs)]  
3. [Indice 3 : Ajouter seulement les chiffres rouges qui ont un certain pattern...]
4. [Indice 4 : Si la taille du carré est n=2k+1 (impair). on remarque que pour calculer le rang suivant 2k+3, on doit ajouter n+1 pour les 4 chiffres rouges suivants (25+6,31+6,37+6,43+6), puis n+3 pour former le carré n+2 pour les 4 suivants ainsi de suite...]

---

## ⚡ Pistes d’optimisation  
- **La récurrence**  
  [La compléxité est en O(n) avec n la taille du carré, ce qui est très rapide. Cela évite de construire un tableau en n^2.] 

---
