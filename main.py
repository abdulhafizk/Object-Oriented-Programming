class Player:
    def __init__(self, health=100, energy=100):
        self.health = health
        self.energy = energy
        print(f"player ceated")

    def attack(self, monster, damage=1):
        self.health -= damage
        self.energy -= damage
        print("attacking!!")

class Monster :
    def __init__(self, health=100):
        self.health = health
        print("monster Created")

player = Player()
monster = Monster(health=500)

player.attack(monster, damage=80)
print(monster.__dict__)