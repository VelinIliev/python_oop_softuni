class Player:
    def __init__(self, name: str, hp: int, mp: int):
        name = name
        hp = hp
        mp = mp
        skills = {}
        guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in skills:
            return f'Skill already added'
        else:
            skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {name}"

    def player_info(self):
        return_string = ""
        return_string += f"Name: {name}\n"
        return_string += f"Guild: {guild}\n"
        return_string += f"HP: {hp}\n"
        return_string += f"MP: {mp}\n"
        for skill, mana in skills.items():
            return_string += f'==={skill} - {mana}\n'
        return return_string

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())