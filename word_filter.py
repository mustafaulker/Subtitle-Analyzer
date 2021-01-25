f = open('./lists/filter_words.txt', "r")
filter_words = f.readlines()
f.close()

buzzkills = []
# Separate words and assign them as lists.
for line in filter_words:
    buzzkills += line.split()

# Encoding for unwanted shapes, decoding for restore data type.
for k in range(len(buzzkills)):
    buzzkills[k] = buzzkills[k].encode("ascii", errors="ignore")
    buzzkills[k] = buzzkills[k].decode().lower()

# Filter empty list elements.
buzzkills = list(filter(None, buzzkills))

# Replacing ';' with ''.
for j in range(len(buzzkills)):
    buzzkills[j] = buzzkills[j].replace(";", '')


# Filter input list with buzzkill list.
def filter_contractions(to_be_filtered):
    return [i for i in to_be_filtered if i not in set(buzzkills)]
