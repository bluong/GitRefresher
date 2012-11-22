import random

class Soldier:
    def __init__(self, health, skill_dict):
        self.health = health
        self.skills = skill_dict

    def choose_skill(self):
        return self.skills[random.choice(self.skills.keys())]
      
    def receive_damage(self, dmg):
        self.health -= dmg
        
    def regenerate(self, life):
        self.health += life
        
    def is_incapacitated(self):
        return self.health <= 0