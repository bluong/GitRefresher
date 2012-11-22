For this assignment, you will be making a turn-based battle system of 2 soldiers.
You should be working in a group of 2, where one person will write code for half and the other will write code for the other half.

First things first, you should have a file called battle.py to write this.
Note this is not in the directory.  You have to add the file to the git repo yourself.
Please do not change battle_runner.py unless you want to implement your own version.

Please have a slight discussion on how the constructor/data structures will be set up.
Also, have a single person write the constructor.

For person A, please write:
parse_soldiers(), a method that will take in a file and parse the soldier's health.
The file format will be like so:
SoldierName{SPACE}Health{NEWLINE}SoldierName{SPACE}Health

get_current_soldier(), a method that will return the soldier who has his turn right now

exchange_attacks(), a method that will run through the process of a soldier attacking the other

gameover(), a method that will return True if the battle is complete

For person B, please write:
parse_skills(), a method that will take in a file and parse the skill name and the damage for that skill for a specific soldier.
The file format will be like so:
Skill1NameForSoldier1{SPACE}SkillDamage;Skill2NameForSoldier1{SPACE}SkillDamage{NEWLINE}
Skill1NameforSoldier2{SPACE}SkillDamage;Skill2NameForSoldier2{SPACE}SkillDamage

process_random_attack(), a method that will simulate the damage exchange between the two soldiers

heal_current_soldier(), a method that will have the current soldier heal a given amount with a certain probability.  For now, make it a static value of 5.

change_turns(), a method that will allow the next soldier to take his turn

After you implement all of the methods with print statements to make your code actually output something, please tag and push.