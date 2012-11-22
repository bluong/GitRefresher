from battle import Battle
import time

SOLDIER_FILE = "soldiers.txt"
SKILL_FILE = "skills.txt"
TURN_DELAY = 1

def battle_start():
    skirmish = Battle(SOLDIER_FILE, SKILL_FILE)
    while (not skirmish.gameover()):
        battle.heal_current_soldier()
        battle.exchange_attacks()
        battle.change_turns()
        time.sleep(TURN_DELAY)
  
if __name__ == '__main__':
    battle_start()
  