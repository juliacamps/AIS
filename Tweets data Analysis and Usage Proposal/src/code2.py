import os

raw_path = os.getcwd()+r"\raw_dataset.json"
parsed_path = os.getcwd()+r"\twitter_dataset.json"
with open(raw_path, 'rb') as raw_file:
    raw_content = raw_file.read()

aux1 = raw_content.decode("utf-8")
aux2 = aux1.split("\n")

aux2 = list(set(aux2))

data = ("\n".join(aux2))
with open(parsed_path, 'wb') as parsed_file:
    parsed_file.write(str.encode(data))
print("parsing performed: OK")