import random

#ENEMY CLASS INITIALISATION
class Enemy:
    def __init__(self, name, hp, hp_max, attack_power, defense, xp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.attack_power = attack_power
        self.defense = defense
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

#ATTACK FUNCTION
    def attack(self, target):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.hp -= damage
        print (f"{self.name} attacks {target.name} for {damage} damage!")

#CHECK IF CHARACTER IS ALIVE FUNCTION
    def is_alive(self):
        return self.hp > 0
    
#SHOW AND PRINT STATS OF CHARACTER (TRY TO FIND A WAY TO ALIGN THE TEXT)
    def show_stats(self):
        print (f"II {self.name} II ")
        print (f"HP : {self.hp} / {self.hp_max} ")
        print (f"Attack : {self.attack_power} I Defense : {self.defense}")