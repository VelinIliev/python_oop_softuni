from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expenses = 200000

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0
        if race_pos <= 1:
            earned_money += 1000000
        elif race_pos <= 3:
            earned_money += 500000
        if race_pos <= 5:
            earned_money += 100000
        elif race_pos <= 7:
            earned_money += 50000
        revenue = earned_money - self.expenses
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
