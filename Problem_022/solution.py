import time

def main():
    start_time1 = time.time()

    # Ouvrir le fichier en mode lecture
    with open('C:/Users/xsy61/Downloads/0022_names.txt', 'r') as fichier:
        # Lire toutes les lignes du fichier
        lignes = fichier.readlines()

        if len(lignes) > 0:
            # Diviser la première ligne en éléments séparés par une virgule
            list = lignes[0].split(",")
                
            # Enlever les doubles guillemets entourant chaque prénom
            new = [name.strip('"') for name in list]
                
            print(f"Liste après suppression des guillemets extérieurs : {new}")
        else:
            print("Le fichier est vide ou n'a pas été lu correctement.")
    scores=0

    n = len(new)
    for i in range(n):
        for j in range(n - i - 1):
            if new[j] > new[j + 1]:
                new[j], new[j + 1] = new[j + 1], new[j]
    print(new)

    for i in range(len(new)):
        sum=0
        if i==938:
            print(new[i])
        for j in range(len(new[i])):
            sum+=ord(new[i][j].lower()) - ord('a') + 1
        scores=scores+(i+1)*sum
    print(scores)
        

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()