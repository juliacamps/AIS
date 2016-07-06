import os

count = 0
aux = []

raw_path = os.getcwd()+r"\castells_twitter_dataset.json"
parsed_path = os.getcwd()+r"\castellers_tweets.txt"
with open(raw_path, 'rb') as raw_file:
    for raw_content in raw_file:
        item = raw_content.decode("utf-8")
        index = item.find("author=", 0, len(item))
        if index > 0:
            index = item.find("id_str=", index, len(item))
            if index > 0:
                index = item.find("screen_name='", index, len(item))
                if index > 0:
                    iter1 = index + len("screen_name='")
                    iter2 = item.find("', ", iter1, len(item))
                    if iter2 > 0 and iter1 < iter2:
                        user_name = item[iter1:iter2]

                        index = item.find("text='", 0, len(item))
                        if index > 0:
                            iter1 = index + len("text='")
                            iter2 = item.find("', ", iter1, len(item))
                            if iter2 > 0 and iter1 < iter2:
                                user_text = item[iter1:iter2]
                                count += 1
                                aux.append(user_name+";;;;"+user_text)

print(count)
print(len(aux))
aux = list(set(aux))
print(len(aux))
data = ("\n".join(aux))
with open(parsed_path, 'wb') as parsed_file:
    parsed_file.write(str.encode(data))
print("parsing performed: OK")