class Character:
    def __init__(self, name, hp, hp_max, mana, mana_max, attack_power, defense,level=1, xp=0, next_level_xp=100, gold=0, inventory=None, armor_set="leather", spell=None):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.mana = mana
        self.mana_max = mana_max
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.xp = xp
        self.next_level_xp = next_level_xp
        self.gold = gold
        self.inventory = inventory
        self.armor_set = armor_set
        self.spell = spell

    def attack(self, target, attack_power):
        pass

    def cast_spell(self, spell, target):
        pass

    def use_item(self, spell):
        pass

    def equip_armor_set(self, armor_set, defence):
        pass

    def gain_xp(self, xp):
        pass

    def level_up(self, level):
        pass

    def is_alive(self):
        pass

    def show_stats(self):
        pass