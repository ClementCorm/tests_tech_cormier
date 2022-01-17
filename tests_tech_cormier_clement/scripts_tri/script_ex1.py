#-------Python v3.8.10-------#

#Tri du fichier sal.txt en fonction de la 12eme colonne après SAL_GEN


def exercice_un():

#Lecture du fichier sal.txt avec spécification de l'encodage pour le point d'interrogation inversé
    with open("../data/sal.txt", encoding="latin-1") as file:
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

#Création de la nouvelle liste contenant les clients ordonnées en fonction de la 12ème colonne
    sorted_data_clients = sorted(data_clients,key = lambda x: x[11])

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
    sorted_file = open("../results/tri/exercice1.txt","w")
    sorted_file.write(result)
    sorted_file.close()

    return 0

#-------------------Lancement de la fonction-------------------#

exercice_un()

