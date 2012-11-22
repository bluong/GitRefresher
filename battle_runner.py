from battle import Battle

SOLDIER_FILE = "soldiers.txt"
SKILL_FILE = "skills.txt"

def battle_start():
    skirmish = Battle(SOLDIER_FILE, SKILL_FILE)
    while (not skirmish.gameover()):
        battle.exchange_attacks()
        battle.change_turns()
  
if __name__ == '__main__':
    battle_start()
  