from random import randint

crimes = ["robbed","spying on","bullies","cheated on","kidnapped","murdered","robbed","raped","scammed","shot","sexually assaulted","gave bribery to ","assassinated","hacked","stole sensitive data of","violated human rights of"]
punishments = ["execution in private place","forgive","jail","home arrest","whipping punishment","execution in public","make slave","banishment",f"{randint(0,10000)} dollars of fine"]
people = ["children","cowboy","dull","whore","old man","baby girl","baby boy","teenager boy","teenager girl","pimp","mafia worker","femboy","teacher","programmer","philosopher","government","nihilist","pessimist","positivist","camus fanboy","schopenhauer fanboy","solid snake","otacon","mickey mouse","crazy man","crazy woman","grandpa","grandma","Kirsten Dust","David Hayter","Heisenberg","Jesse Pinkman","Mozart","Beethoven","Saul Goodman","duck","cat","Jesus","Rustin Cohle","Moses","Mohammad","Erdogan","Putin","Jim Carey","Kojima"]

def chose_crime():
    i = randint(0,15)
    return crimes[i]
def chosePeople():
    p = randint(0,44)
    return people[p]
def choosePunishment():
    k = randint(0,8)
    return punishments[k]
def chooseTime():
    t = randint(0,4)
    return t

def start():
    while True:
        print(chosePeople(),chose_crime(),chosePeople())
        print("[1]",choosePunishment())
        print("[2]",choosePunishment())
        print("[3]",choosePunishment())
        print("[4] exit")
        decade = int(input('Enter your decision: '))
        if decade == 4:
           exit()
        else:
            continue
        
start()
    
    