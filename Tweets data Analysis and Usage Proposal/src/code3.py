import os
import json
from collections import Counter

parsed_path = os.getcwd()+r"\twitter_dataset.json"
collected_users_path = os.getcwd()+r"\users_dataset.txt"

threshold = 2 # As has been defined in the associated paper


with open(parsed_path, 'rb') as parsed_file:
   data_lines = ((parsed_file.read()).decode("utf-8")).split("\n")
count = 0
users_aux = []
for line in data_lines:
    index = line.find("author=", 0, len(line))
    if index > 0:
        index = line.find("id_str=",index,len(line))
        if index > 0:
            index = line.find("screen_name='", index, len(line))
            if index>0:
                iter1 = index+len("screen_name='")
                iter2 = line.find("', ", iter1, len(line))
                if iter2 > 0 and iter1<iter2:
                    user_name = line[iter1:iter2]
                    if (user_name.lower()).find("diari") == -1 and (user_name.lower()).find("info") == -1 and \
                                    (user_name.lower()).find("radio") == -1 and (user_name.lower()).find("tv") == -1:
                        count+=1
                        users_aux.append(user_name)
freq = Counter(users_aux)
users = []

for user in freq:
    if freq[user]>=threshold:
        users.append(user)
print(len(users))
print(count)

with open(collected_users_path, 'wb') as collected_users_file:
    collected_users_file.write(str.encode("\n".join(users)))
print("parsing performed: OK")
