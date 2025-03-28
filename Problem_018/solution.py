import time

def max_path_sum(triangle):
    """ Calcule la somme maximale d'un chemin du haut vers le bas en utilisant la programmation dynamique. """
    # On part du bas et on remonte
    for i in range(len(triangle) - 2, -1, -1):  # Parcours des lignes de bas en haut
        for j in range(len(triangle[i])):  # Parcours des éléments de la ligne
            # Mise à jour de la cellule avec le meilleur choix en dessous
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    # La racine contient la somme maximale
    return triangle[0][0]

def main():
    start_time = time.time()


    with open("D://Project-Euler//0067_triangle.txt","r",encoding="utf-8") as fichier:
        lignes = fichier.readlines()


    string = "".join(lignes).strip()  # On utilise strip() pour enlever les espaces superflus à la fin

    print(string)
    # Transformer le texte en liste de listes (matrice triangulaire)
    triangle = [list(map(int, row.split())) for row in string.split("\n")]

    # Résolution par programmation dynamique
    max_sum = max_path_sum(triangle)

    print(f"\nLa somme maximale du chemin est : {max_sum}")

    # Temps d'exécution
    elapsed_time = time.time() - start_time
    print(f"Le code a pris {elapsed_time:.5f} secondes à s'exécuter.")

if __name__ == '__main__':
    main()
