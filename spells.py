import random

#SPELL CLASS INITIALISATION
class Spell :
    def __init__(self, name, mana_cost, damage, is_available = True ):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.is_available = is_available

 #CAST SPELL TO ENEMY FUNCTION       
    def cast(self, caster, target):
        if self.is_available:
            total = self.damage + caster.spell_power 
            damage = random.randint(total - 10, total + 10)
            target.hp -= damage
            print(f"{caster.name} casts {self.name} on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} is not available!")