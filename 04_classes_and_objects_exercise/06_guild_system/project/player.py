class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return f'Skill already added'
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        return_string = ""
        return_string += f"Name: {self.name}\n"
        return_string += f"Guild: {self.guild}\n"
        return_string += f"HP: {self.hp}\n"
        return_string += f"MP: {self.mp}\n"
        for skill, mana in self.skills.items():
            return_string += f'==={skill} - {mana}\n'
        return return_string

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())