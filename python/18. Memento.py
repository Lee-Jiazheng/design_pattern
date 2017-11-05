'''Memento

'''
class Player():
    def __init__(self):
        self.viality = 100
        self.attack = 100
        self.defense = 100
    def RecoveryState(self, memento):
        self.viality = memento.viality
        self.attack = memento.attack
        self.defense = memento.defense
    def DisplayState(self):
        print("Player's State")
        print("Viality is %s" % self.viality)
        print("Attack is  %s" % self.attack)
        print("Defense is %s" % self.defense)
    def SaveState(self):
        return RoleStateMemento(self.viality, self.attack, self.defense)
    def Fight(self):
        print("I'm Fighting...")
        self.viality = 0
        self.attack = 0
        self.defense = 0

class RoleStateMemento:
    def __init__(self, v, a, d):
        self.viality = v
        self.attack = a
        self.defense = d

# The class manages the role's state
class RoleStateCaretaker:
    def __init__(self, mem):
        self.memento = mem

if __name__ == "__main__":
    player = Player()
    player.DisplayState()
    stateCaretaker = RoleStateCaretaker(player.SaveState())
    player.Fight()
    player.DisplayState()
    player.RecoveryState(stateCaretaker.memento)
    player.DisplayState()
    