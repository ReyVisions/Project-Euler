# 🔢 Projet Euler – Problème *27*  

## 📊 Estimation de la difficulté  
👉 **5% – [->>Très facile / Facile / Moyen / Difficile / Très difficile]** 

---

## 💡 Idée générale  
L’objectif est de traduire directement l’énoncé mathématique en un programme informatique.  
Le problème repose essentiellement sur l’évaluation de trinomiales du second degré et sur la détection des nombres premiers.  

---

## 🚀 Stratégie de résolution  
1. Parcourir les paramètres possibles du polynôme.  
2. Vérifier si les valeurs générées sont des nombres premiers.  
3. Maximiser le critère demandé (ex. longueur de suite de nombres premiers).  

---

## ⚡ Pistes d’optimisation  
- **Test de primalité**  
  Utiliser la division d’essai **jusqu’à √n** pour vérifier si un nombre est premier.  
  > Complexité réduite de \(O(n)\) à \(O(\sqrt{n})\).  

- **Réduction du domaine de recherche**  
  - On peut ignorer les valeurs de \(b\) négatives : en effet, pour \(n=0\), la valeur du trinôme serait négative.  
  - Se limiter aux trinomiales qui produisent des valeurs positives (discriminant \(\Delta \leq 0\)).  

- **Amélioration pratique**  
  - Générer uniquement les polynômes du second degré ayant une chance de produire plusieurs nombres premiers.  
  - Stocker les résultats de primalité déjà calculés (mémoïsation / crible) pour accélérer le programme.  

---
