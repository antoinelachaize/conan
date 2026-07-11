from characters import Character
from enemies import Enemy


def fight(hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        hero.attack(enemy)
        if not enemy.is_alive():
            print (f"{hero.name} win the fight ! {enemy.name} was defeated !")
            break
        else:
            enemy.attack(hero)
            if not hero.is_alive():
                print (f"{enemy.name} win the fight ! {hero.name} was defeated !")

        
