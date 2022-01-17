#-------Python v3.8.10-------¿



#Fonction permettant de concaténer une liste avec rajoutant les séparateurs '¿' et 'X_GEN' utilisée avant l'écriture des fichiers de sorties
def formatage(liste):
    result = "SAL_GEN"
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


def exercice_un():

#Lecture du fichier sal.txt
    with open("../data/sal.txt",encoding="latin-1") as file:
        data = file.read()

#Création d'une liste des différents clients en découpant les données autour des SAL_GEN
    list_clients = data.split("SAL_GEN")

#Je retire la ligne html qui a été ajoutée au dernier client
    list_clients[len(list_clients)-1] = list_clients[len(list_clients)-1].split("<compteur>")[0]

#Je retire également la première entrée qui est vide puisqu'elle est avant le premier SAL_GEN
    list_clients = list_clients[1:]

#Pour chaque client, je construit une liste de ses différents champs en séparés du ¿
    data_clients = []
    for i in range(len(list_clients)):
        data_clients.append(list_clients[i].split("¿"))
        data_clients[i] = data_clients[i][1:]

#Création des deux listes pour la séparation des entrées
    list_M = []
    list_others = []

#On ajoute dans la première ou deuxième liste en fonction de la valeur de la colonne 13
    for i in range(len(data_clients)):
        if data_clients[i][13] == "M.":
            list_M.append(data_clients[i])
        else:
            list_others.append(data_clients[i])

#On reformate les listes
    list_M_form = formatage(list_M)
    list_others_form = formatage(list_others)

#On écrit les données triées dans un fichier qui sera créé dans le dossier results/filtre/exo1 pour chacune des listes
    sorted_file = open("../results/filtre/exo1/exercice1_M.txt","w")
    sorted_file.write(list_M_form)
    sorted_file.close()

    sorted_file = open("../results/filtre/exo1/exercice1_others.txt","w")
    sorted_file.write(list_others_form)
    sorted_file.close()


    return 0

#-------------------Lancement de la fonction-------------------#

exercice_un()

