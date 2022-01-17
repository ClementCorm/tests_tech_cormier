#-------Python v3.8.10-------#

import sys,re

#Fonction permettant de concaténer une liste avec rajoutant les séparateurs '¿' et 'X_GEN' utilisée avant l'écriture des fichiers de sorties
def formatage(liste):

#On vérifie que la liste n'est pas vide
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


def exercice_quatre(enregistrement, position, valeur):

#Lecture du fichier sal.txt avec l'encodage 'latin-1' pour pas que le caractère ¿ ne pose problème
    with open("../data/sal.txt", encoding="latin-1") as file:
        data = file.read()

#Lecture du fichier ent.txt
    with open("../data/ent.txt", encoding="latin-1") as file_ent:
        data_ent = file_ent.read()

#On vérifie que l'enregistrement passé en argument existe et si c'est le cas, si il provient du fichier client ou du fichier entreprise
    if "\n" + enregistrement in data_ent:
        enregistrement_client = False
    elif "\n" + enregistrement in data:
        enregistrement_client = True
    else:
        print("Enregistrement introuvable")
        return 0

#Création d'une liste des différents clients en découpant les données sur "SAL_GEN"
    list_clients = data.split("SAL_GEN")

#On retire la ligne html qui a été ajoutée au dernier client
    list_clients[len(list_clients)-1] = list_clients[len(list_clients)-1].split("<compteur>")[0]

#On retire également la première entrée qui est vide puisqu'elle est avant le premier séparateur
    list_clients = list_clients[1:]

#Pour chaque client, on construit une liste de ses différents champs séparés par le caractère ¿
    data_clients = []
    for i in range(len(list_clients)):
        data_clients.append(list_clients[i].split("¿"))
        data_clients[i] = data_clients[i][1:]


#Création d'une liste des différentes entreprises de la même manière
    list_ent = data_ent.split("ENT_GEN")

    list_ent = list_ent[1:]

    data_ent = []
    for i in range(len(list_ent)):
        data_ent.append(list_ent[i].split("¿"))
        data_ent[i] = data_ent[i][1:]

#On compile l'expression rationnelle passée en argument pour pouvoir la comparer aux données
    pattern = re.compile(valeur)

#Si l'enregistrement provient du fichier entreprise, on crée une liste des id pour lesquels la donnée recherchée match avec la bonne colonne 
    if not enregistrement_client:
        ids_ent = []

#Pour chaque entreprise, on va chercher la position exacte de la colonne contenant le nom de l'enregistrement
#puis incrémenter cette position en fonction de la colonne passée en argument
        for i in range(len(data_ent)):
            index_colonne = 0
            for y in range(len(data_ent[i])):
                if data_ent[i][y] == ("\n" + enregistrement):
                    index_colonne = y
            index_colonne += position
#On décrémente une fois l'index de la colonne puisque les "ENT_GEN" ont été retirés
            if enregistrement == "ENT_GEN":
                index_colonne -= 1
#On vérifie que la donnée match le pattern, si c'est le cas l'id de l'entreprise est ajouté à la liste
            if pattern.match(data_ent[i][index_colonne]):
                ids_ent.append(data_ent[i][1])


#Création des deux listes pour la séparation des entrées
    list_a = []
    list_b = []

#Dans le cas où l'enregistrement provient du fichier client
    if enregistrement_client:
#On récupère selon la même logique précédente la position exacte de la colonne recherchée dans notre liste
        for i in range(len(data_clients)):
            index_enreg = 0
            for y in range(len(data_clients[i])):
                if data_clients[i][y] == ("\n" + enregistrement):
                    index_enreg = y
            index_colonne = index_enreg + position
            if(enregistrement == "SAL_GEN"):
                index_colonne -= 1
#Si la donnée match avec le pattern, elle va dans la première liste. Sinon, dans la deuxième
            if pattern.match(data_clients[i][index_colonne]):
                list_a.append(data_clients[i])
            else:
                list_b.append(data_clients[i])

#Dans le cas d'un enregistrement d'entreprise en paramètre, on récupère tous les clients dont l'id de la deuxième colonne est présent dans la liste des id
    else:
        for i in range(len(data_clients)):
            if data_clients[i][1] in ids_ent:
                list_a.append(data_clients[i])
            else:
                list_b.append(data_clients[i])

#On reformate les listes
    list_a_form = formatage(list_a)
    list_b_form = formatage(list_b)

#On écrit les données triées dans deux fichiers qui seront créés dans le dossier results/filtre/exo4 pour chacune des listes
    sorted_file = open("../results/filtre/exo4/exercice4_a.txt","w")
    sorted_file.write(list_a_form)
    sorted_file.close()

    sorted_file = open("../results/filtre/exo4/exercice4_b.txt","w")
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
    exercice_quatre(enregistrement, position, valeur)

