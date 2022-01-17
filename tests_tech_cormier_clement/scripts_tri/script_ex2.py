#-------Python v3.8.10-------¿

import sys

def exercice_deux(enregistrement, champ):

#Lecture du fichier sal.txt avec spécification de l'encodage pour le point d'interrogation inversé
    with open("../data/sal.txt", encoding="latin-1") as file:
        data = file.read()

#On vérifie que l'enregistrement passé en argument existe
    if "\n" + enregistrement not in data:
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
    sorted_file = open("../results/tri/exercice2.txt","w")
    sorted_file.write(result)
    sorted_file.close()
    return 0


#-------------------Lancement de la fonction-------------------#
if len(sys.argv) != 3:
    print("Veuillez entrer l'enregistrement et la position du champ")
else:
    enregistrement = sys.argv[1]
    champ = int(sys.argv[2])
    exercice_deux(enregistrement, champ)

