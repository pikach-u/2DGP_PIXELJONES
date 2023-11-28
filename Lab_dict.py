import pickle
class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name


# npc1 = NPC(100, 200, 'jenni')
# print(type(npc1.__dict__)) #객체의 속성값을 dictonary 형태로 가지고 있음. 따라서 속성값을 update로도 변경 가능
# print(npc1.__dict__)
#
# #두 코드가 같다
# npc1.x = 200
# npc1.__dict__.update({'x':200})

npc1 = NPC(100, 200, 'jenni')
npc2 = NPC(500, 100, 'zwi')


group = [npc1, npc2] #하나로 묶어서 저장해준다
with open('npc.pickle', 'wb') as f: #객체를 binary로 저장
    pickle.dump(group, f)

