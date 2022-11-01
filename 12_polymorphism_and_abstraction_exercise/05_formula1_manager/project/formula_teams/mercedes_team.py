from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        expenses = 200000
        sponsors = 0
        if race_pos == 1:
            sponsors += 1000000
        elif race_pos <= 3:
            sponsors += 500000
        if race_pos <= 5:
            sponsors += 100000
        elif race_pos <= 7:
            sponsors += 50000
        revenue = sponsors - expenses
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'