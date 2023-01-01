def get_none():
    return None

def flatten_dict(dictionary):
    if isinstance(dictionary, dict):
        return list(dictionary.values())
    else:
        return "Only dictonary is alowed"

    
test_dic = {"book1" : "Armagedon", "book2" : "Paradise", "book3": [20,11,34]}

print(flatten_dict(test_dic))