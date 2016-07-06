import os

football_count = 0
climbing_count = 0
volleyball_count = 0

football_vocabulary = ["delantero","gol","partit","media parte","cristiano","messi","FCB","Madrid","atletic","neymar",
                       "liga","champions","copa","ramos","cule","bernabeu","camp nou","guardiola","pique","futbol","football",
                       "arbitro","colegiado","penalti","saque","campo","falta"]
climbing_vocabulary = ["encadenar","esportiva","escalada","cinta","arnes","corda","de primero","cresta","boulder","presa",
                       "caida","atar","de segundo","Siurana","escalada","climbing","pies de gato","grigri","casco","via larga",
                       "clasica","deportiva","escalador","subir"]
volleyball_vocabulary = ["Zagueros","Varillas","Tie-break","Set","Ratocion","Retencion","Remate","Recepcion",
                         "Tercer tiempo","Segundo tiempo","Primer tiempo","Plancha","Invacion","Flotante","Finta",
                         "Dobles","Delanteros","Colocacion","Caida","Bloqueo","Apoyo","punto","voley","playa","volleyball",
                         "central","punta","opuesta","saque","linea","torneo"]

data_path = os.getcwd()+r"\castellers_tweets.txt"

with open(data_path, 'rb') as data_file:
    data_lines = (((data_file.read()).decode("utf-8")).lower()).split("\n")

for line in data_lines:
    football_index = -1
    climbing_index = -1
    volleyball_index = -1
    it = 0
    ini = line.find(";;;;", 0, len(line))+len(";;;;")
    while football_index < 0 and it<len(football_vocabulary):
        football_index = line.find(football_vocabulary[it].lower(), ini, len(line))
        it += 1
    if football_index > 0:
        football_count += 1

    it = 0
    while climbing_index < 0 and it < len(climbing_vocabulary):
        climbing_index = line.find(climbing_vocabulary[it].lower(), ini, len(line))
        it += 1
    if climbing_index > 0:
        climbing_count += 1

    it = 0
    while volleyball_index < 0 and it < len(volleyball_vocabulary):
        volleyball_index = line.find(volleyball_vocabulary[it].lower(), ini, len(line))
        it += 1
    if volleyball_index > 0:
        volleyball_count += 1

print("Football presence: "+str(football_count/len(data_lines)))
print("Climbing presence: "+str(climbing_count/len(data_lines)))
print("Volleyball presence: "+str(volleyball_count/len(data_lines)))

print("Total instances: "+str(len(data_lines)))