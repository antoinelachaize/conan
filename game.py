from characters import Character
from enemies import Enemy

#MAIN FIGHT FUNCTION LOOP
def fight(hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        print("1) Attack with your weapon")
        print("2) Cast a spell")
        choice = int (input("What do you want to do ?"))
        if choice == 1:
            hero.attack(enemy)
        elif choice == 2:
            hero.spell[0].cast(hero, enemy)
        if not enemy.is_alive():
            print (f"{hero.name} win the fight ! {enemy.name} was defeated !")
            break
        else:
            enemy.attack(hero)
            if not hero.is_alive():
                print (f"{enemy.name} win the fight ! {hero.name} was defeated !")

        
