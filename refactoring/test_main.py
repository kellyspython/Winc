__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

class HomeOwner:
    def __init__(self, name, adres, needs):
        self.name = name
        self.adres = adres
        self.needs = needs
        
        
    def __str__(self):
        return f'Homeowner({self.name},{self.adres},{self.needs})'


class Specialist():
    def __init__(self, name, specialisme):
        self.name = name
        self.specialisme = specialisme

        
class Electrician(Specialist):
    def __init__(self, name, price):
        super().__init__(name, 'electrician')
        self.price = price
    

class Painter(Specialist):
    def __init__(self, name, price):
        super().__init__(name, 'painter')
        self.price = price

class Plumber(Specialist):
    def __init__(self, name, price):
        super().__init__(name, 'plumber')
        self.price = price



alfred = HomeOwner("Alfred Alfredson","Alfredslane 123",["painter", "plumber"])
bert = HomeOwner("Alfred Alfredson","Bertslane 231",["plumber"])
candice = HomeOwner("Candice Candicedottir","Candicelane 312",["electrician", "painter"])


alice = Electrician("Alice Aliceville", 20)
kelly = Electrician("Kelly van Wijk", 21)
bob = Painter("Bob Bobsville", 30)
craig = Plumber("Craig Craigsville",25)

#print(f"{alice.name}, {alice.specialisme}, € {alice.price}")

def contracts():
    alfred_contracts = []
    for need in alfred.needs:
        if need == alice.specialisme or kelly.specialisme:
            if alice.price < kelly.price:
                alfred_contracts.append(alice.name)
            else:
                alfred_contracts.append(kelly.name)
        elif need == bob.specialisme:
            alfred_contracts.append(bob.name)
        elif need == craig.specialisme:
            alfred_contracts.append(craig.name)

    bert_contracts = []
    for need in bert.needs:
        if need == alice.specialisme:
            bert_contracts.append(alice.name)
        elif need == bob.specialisme:
            bert_contracts.append(bob.name)
        elif need == craig.specialisme:
            bert_contracts.append(craig.name)

    candice_contracts = []
    for need in candice.needs:
        if need == alice.specialisme:
            candice_contracts.append(alice.name)
        elif need == bob.specialisme:
            candice_contracts.append(bob.name)
        elif need == craig.specialisme:
            candice_contracts.append(craig.name)

    print("Alfred's contracts:", alfred_contracts)
    print("Bert's contracts:", bert_contracts)
    print("Candice's contracts:", candice_contracts)
contracts()