def test_get_none():
    return None

def test_flatten_dict(dictionary):
    if isinstance(dictionary, dict):

        return list(dictionary.values())
    else:
        return "Only dictonary is alowed"


test_dic = {"book1" : "Armagedon", "book2" : "Paradise", "book3": [20,11,34], "testdict": { "book4": "kellys best"}}
test_list = ["aap", "noot", "mies"]


print(test_flatten_dict(test_dic))