import random
import time

player_HP = 100
player_energy = 0
comp_HP = 100
comp_energy = 0


class Player(): 
    def normal_atk(self):
        attack = random.randint(0, 15)
        return attack
        
    def spec_attack(self):
        spec_atk = random.randint(20, 40)
        return spec_atk

    def heal(self):
        healing = random.randint(5, 25)
        return healing


def first_go():
    go = random.randint(0, 1)
    if go == 0:
        return 'Comp'
    else:
        return name



ready = input("Are you ready to play? Y/N ")
name = input("Please enter your name: ")
turn = first_go()

player = Player()
comp = Player()

comp_attack_normal = comp.normal_atk()
comp_special_attack = comp.spec_attack()
comp_healer = comp.heal()

comp_abilities = [comp_attack_normal, comp_special_attack]

# While player 1 and player 2 HP's are over 0:
while player_HP > 0 and comp_HP > 0:
    print(f"\n{turn}'s turn")
    if turn != 'Comp':
        action = int(input(f"{name}, please choose an action:\n1) Normal Attack\n2) Special Attack\n3) Heal\n"))
        if action == 1:
            player_normal_attack = player.normal_atk()
            comp_HP = comp_HP - player_normal_attack
            player_energy += 10
            time.sleep(1)
            print(f"\n{name} just did {player_normal_attack} damage!")
            print(f"{name} now has {player_HP} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 2 and player_energy >= 20:
            player_special_attack = player.spec_attack()
            comp_HP = comp_HP - player_special_attack
            player_energy -= 20
            time.sleep(1)
            print(f"\n{name} just did {player_special_attack} damage!")
            print(f"{name} now has {player_HP} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_energy} energy")
            turn = 'Comp'
        elif action == 3 and player_energy >= 15:
            player_heal = player.heal()
            player_HP += player_heal
            player_energy -= 15
            time.sleep(1)
            print(f"\n{name} just healed themselves for {player_heal}")
            turn = 'Comp'
        elif action == 2 or action == 3 and player_energy < 10:
            print(f"\n{name} you have {player_HP} health and {player_energy} energy")
            print(f"\n{name} your energy is too low, please choose 1) Normal Attack: ")
        else:
            print(f"Please enter a correct action")
    else:
        if comp_energy >= 20:
            comp_spec_attack = comp.spec_attack()
            player_HP = player_HP - comp_spec_attack
            comp_energy -= 20
            time.sleep(1)
            print(f"\nThe computer just did {comp_spec_attack} damage")
            print(f"{name} now has {player_HP} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_energy} energy")
            turn = name
        elif comp_HP < 40 and comp_energy >= 15:
            comp_healing = comp.heal()
            comp_HP += comp_healing
            comp_energy -= 15
            time.sleep(1)
            print(f"\nThe comp has healed themselves for {comp_healing}")
            print(f"{name} now has {player_HP} health and {player_energy} energy")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_energy} energy")
            turn = name
        else:
            comp_norm_attack = comp.normal_atk()
            player_HP = player_HP - comp_norm_attack
            comp_energy += 10
            time.sleep(1)
            print(f"\nComp just did {comp_norm_attack} damage!")
            print(f"\n{name} now has {player_HP} health and {player_energy} energy")
            print(f"The computer now has {comp_HP} health and {comp_energy} energy")
            turn = name
    
if player_HP <= 0:
    print(f"\nComputer has won this round!")
elif comp_HP <= 0:
    print(f"\n{name} has won this round!")
