#-------Python v3.8.10-------¿

import sys

def exercice_trois(enregistrement, champ):

#Lecture du fichier sal.txt avec spécification de l'encodage pour le point d'interrogation inversé
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

#Création d'une liste des différents clients en découpant les données autour de SAL_GEN
    list_clients = data.split("SAL_GEN")

#Je retire la ligne html qui a été ajoutée au dernier client
    list_clients[len(list_clients)-1] = list_clients[len(list_clients)-1].split("<compteur>")[0]

#Je retire également la première entrée qui est vide puisqu'elle est avant le premier enregistrement
    list_clients = list_clients[1:]

#Pour chaque client, je construit une liste de ses différents champs en séparés du ¿
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

#Dans le cas où l'enregistrement ne provient pas du fichier ent.txt, on fait le même traitement que le script précédent
    if enregistrement_client:
#Les clients n'ayant pas forcément le même nombre de colonne, l'enregistrement passé en paramètre ne sera pas toujours à la même position dans la liste
#On va donc pour chaque client récupérer la n-ième valeur après l'enregistrement passé en paramètre

#Dans le cas où l'enregistrement est SAL_GEN, on a pas ce soucis, on regarde si la donnée est un entier ou une chaîne de caractère puis on trie en fonction
        if enregistrement == "SAL_GEN":
            if data_clients[0][champ - 1].isnumeric():
                sorted_data_clients = sorted(data_clients,key = lambda x: int(x[(champ - 1)]))
            else:
                sorted_data_clients = sorted(data_clients,key = lambda x: x[(champ - 1)])

#Dans l'autre cas, on créé une liste contenant un duo (positionnement du client dans la liste initiale - valeur de la colonne à trier)
#On va ensuite trier cette liste selon la valeur de la colonne à trier
# On finit par itérer sur cette liste en ajoutant dans une nouvelle liste, les données du client en fonction de la position 
        else:
            sorted_data_clients = []
            list_rank_value = []
            for i in range(len(data_clients)):
                for y in range(len(data_clients[i])):
                    if data_clients[i][y] == "\n" + enregistrement:
                        list_rank_value.append([i,data_clients[i][champ + y]])

            if list_rank_value[0][1].isnumeric():
                list_rank_value = sorted(list_rank_value,key = lambda x: int(x[1]))
            else:
                list_rank_value = sorted(list_rank_value,key = lambda x: x[1])
            for i in range(len(list_rank_value)):
                sorted_data_clients.append(data_clients[list_rank_value[i][0]])

#Dans le cas où l'enregistrement provient du fichier ent.txt
    else:
#Si l'enregistrement en paramètre est "ENT_GEN" l'index de la colonne est celui passé en paramètre -1
#Sinon, on va chercher la position de l'enregistrement puis lui ajouter la valeur de la colonne passé en paramètre
        index_colonne_a_trier = 0
        if enregistrement == "ENT_GEN":
            index_colonne_a_trier = champ - 1
        else:
#On boucle seulement sur la 1ere donnée pour récupérer l'index puisque toutes les entreprises ont le même nombre de données
            for i in range(len(data_ent[0])):
                if data_ent[0][i] == "\n" + enregistrement:
                    index_colonne_a_trier = i + champ

#On trie cette colonne en fonction de si c'est un entier ou non
        if data_ent[0][champ - 1].isnumeric():
            sorted_data_ents = sorted(data_ent,key = lambda x: int(x[index_colonne_a_trier]))
        else:
            sorted_data_ents = sorted(data_ent,key = lambda x: x[index_colonne_a_trier])

#On boucle ensuite sur nos données triées puis on récupère les différents id (de façon unique) dans l'ordre d'apparition
        list_id = []
        for i in range(len(sorted_data_ents)):
            if sorted_data_ents[i][1] not in list_id:
                list_id.append(sorted_data_ents[i][1])

#On boucle ensuite sur la liste des id et pour chacun d'entre eux, on va chercher les données clientes correspondantes pour avoir notre liste triée
        sorted_data_clients = []
        for i in range(len(list_id)):
            for y in range(len(data_clients)):
                if data_clients[y][1] == list_id[i]:
                    sorted_data_clients.append(data_clients[y])

#Reconstruction des données en concaténant les différentes listes et en rajoutant les séparateurs
    result = "SAL_GEN"
    for i in range(len(sorted_data_clients)):
        result += "¿"
        for y in range(len(sorted_data_clients[i])):
            result += sorted_data_clients[i][y]
#On s'assure de ne pas rajouter le séparateur pour la dernière ligne
            if y != len(sorted_data_clients[i]) - 1:
                result += "¿"
#Idem
        if i != len(sorted_data_clients) - 1:
            result += "SAL_GEN"

#Rajout du compteur
    count = "<compteur>" + str(len(sorted_data_clients)) + "</compteur>\n"
    result += count

#On écrit les données triées dans un fichier qui sera créé dans le dossier results/tri
    sorted_file = open("../results/tri/exercice3.txt","w")
    sorted_file.write(result)
    sorted_file.close()

    return 0


#-------------------Lancement de la fonction-------------------#

if len(sys.argv) != 3:
    print("Veuillez entrer l'enregistrement et la position du champ")
else:
    enregistrement = sys.argv[1]
    champ = int(sys.argv[2])
    exercice_trois(enregistrement, champ)

