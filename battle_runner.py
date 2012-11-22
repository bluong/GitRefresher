from battle import Battle
import time

SOLDIER_FILE = "soldiers.txt"
SKILL_FILE = "skills.txt"

def battle_start():
    skirmish = Battle(SOLDIER_FILE, SKILL_FILE)
    while (not skirmish.gameover()):
        battle.heal_current_soldier()
        battle.exchange_attacks()
        battle.change_turns()
        time.sleep(1)
  
if __name__ == '__main__':
    battle_start()
  