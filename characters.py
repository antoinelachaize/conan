import random

#CHARACTER CLASS INITIALISATION
class Character:
    def __init__(self, name, hp, hp_max, mana, mana_max, attack_power, spell_power, defense,level=1, xp=0, next_level_xp=100, gold=0, inventory=None, armor_set="leather", spell=None):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.mana = mana
        self.mana_max = mana_max
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.defense = defense
        self.level = level
        self.xp = xp
        self.next_level_xp = next_level_xp
        self.gold = gold
        self.inventory = inventory if inventory is not None else []
        self.armor_set = armor_set
        self.spell = spell if spell is not None else []

#ATTACK FUNCTION
    def attack(self, target):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.hp = target.hp - damage
        print (f"{self.name} attacks {target.name} for {damage} damage!")

#USE ITEM FUNCTION
    def use_item(self, item):
        self.hp = self.hp + item.value
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print (f"You drink {item.name} and you heal for {item.value} HP !")

#EQUIP ARMOR FUNCTION 
    def equip_armor_set(self):
        pass

#GAIN XP FUNCTION
    def gain_xp(self):
        pass

#LEVEL UP FUNCTION
    def level_up(self):
        pass

#CHECK IF CHARACTER IS ALIVE FUNCTION
    def is_alive(self):
        return self.hp > 0

#SHOW AND PRINT STATS OF CHARACTER (TRY TO FIND A WAY TO ALIGN THE TEXT)
    def show_stats(self):
        print (f"II {self.name} II ")
        print (f"HP : {self.hp} / {self.hp_max} I MANA : {self.mana} / {self.mana_max}")
        print (f"Attack : {self.attack_power} I Spell Power : {self.spell_power} I Defense : {self.defense} I Level : {self.level}")