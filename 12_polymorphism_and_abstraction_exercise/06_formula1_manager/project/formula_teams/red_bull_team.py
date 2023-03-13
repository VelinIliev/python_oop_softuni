from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expenses = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0
        if race_pos <= 1:
            earned_money += 1500000
        elif race_pos <= 2:
            earned_money += 800000
        if race_pos <= 8:
            earned_money += 20000
        elif race_pos <= 10:
            earned_money += 10000
        revenue = earned_money - self.expenses
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
