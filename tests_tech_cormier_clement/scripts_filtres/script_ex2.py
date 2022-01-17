#-------Python v3.8.10-------#
import sys


#Fonction permettant de concaténer une liste avec rajoutant les séparateurs '¿' et 'X_GEN' utilisée avant l'écriture des fichiers de sorties
def formatage(liste):
    if(len(liste) != 0):
        result = "SAL_GEN"
    else:
        result = ""
    for i in range(len(liste)):
        result += "¿"
        for y in range(len(liste[i])):
            result += liste[i][y]
#On s'assure de ne pas rajouter le séparateur pour la dernière ligne
            if y != len(liste[i]) - 1:
                result += "¿"
#Idem
        if i != len(liste) - 1:
            result += "SAL_GEN"

#Rajout du compteur du nombre d'entrées
    count = "<compteur>" + str(len(liste)) + "</compteur>\n"
    result += count
    return result




def exercice_deux(enregistrement, position, valeur):

#Lecture du fichier sal.txt
    with open("../data/sal.txt", encoding="latin-1") as file:
        data = file.read()

#On vérifie que l'enregistrement passé en argument existe
    if "\n" + enregistrement not in data:
        print("Enregistrement introuvable")
        return 0

#Création d'une liste des différents clients en découpant les données
    list_clients = data.split("SAL_GEN")

#Je retire la ligne html qui a été ajoutée au dernier client
    list_clients[len(list_clients)-1] = list_clients[len(list_clients)-1].split("<compteur>")[0]

#Je retire également la première entrée qui est vide puisqu'elle est avant le premier séparateur
    list_clients = list_clients[1:]

#Pour chaque client, je construit une liste de ses différents champs en séparés du ¿
    data_clients = []
    for i in range(len(list_clients)):
        data_clients.append(list_clients[i].split("¿"))
        data_clients[i] = data_clients[i][1:]


#Création des deux listes pour la séparation des entrées
    list_a = []
    list_b = []

#On ajoute dans la première ou deuxième liste en fonction de la valeur de la colonne passée en entrée
    for i in range(len(data_clients)):
        index_enreg = 0
        for y in range(len(data_clients[i])):
            if data_clients[i][y] == ("\n" + enregistrement):
                index_enreg = y
        index_colonne = index_enreg + position
        if (enregistrement == "SAL_GEN"):
            index_colonne -= 1
        if data_clients[i][index_colonne] == valeur:
            list_a.append(data_clients[i])
        else:
            list_b.append(data_clients[i])

#On reformate les listes
    list_a_form = formatage(list_a)
    list_b_form = formatage(list_b)

#On écrit les données triées dans des fichiers qui seront créés dans le dossier results/filtre/exo2 pour chacune des listes
    sorted_file = open("../results/filtre/exo2/exercice2_a.txt","w")
    sorted_file.write(list_a_form)
    sorted_file.close()

    sorted_file = open("../results/filtre/exo2/exercice2_b.txt","w")
    sorted_file.write(list_b_form)
    sorted_file.close()


    return 0

#-------------------Lancement de la fonction-------------------#

#Vérification que le bon nombre d'argument est passé en entrée du script
if len(sys.argv) != 4:
    print("Veuillez préciser l'enregistrement, la position du champ ainsi que la valeur recherchée")
else:
    enregistrement = sys.argv[1]
    position = int(sys.argv[2])
    valeur = sys.argv[3]
    exercice_deux(enregistrement, position, valeur)

