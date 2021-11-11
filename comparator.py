from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return "(" + self.name + ": " + str(self.score) + ")"
        
    def comparator(a, b):
        if a.score != b.score:
            return a.score - b.score 
        else:
            i = 0
            while(i < len(a.name) and i < len(b.name)):
                if a.name[i] > b.name[i]:
                    return 1
                elif a.name[i] < b.name[i]:
                    return -1
                else:
                    i += 1
            if i < len(a.name):
                return 1
            elif i < len(b.name):
                return -1
            else:
                return 0

data = []
data.append(Player('amy',100))
data.append(Player('adavid',100))
data.append(Player('aheraldo',50))
data.append(Player('aheraldoo',50))
data.append(Player('aheraldoa',50))
data.append(Player('aheraldoa',50))
data.append(Player('aaakansha',75))
data.append(Player('aaleksa',150))

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
    
