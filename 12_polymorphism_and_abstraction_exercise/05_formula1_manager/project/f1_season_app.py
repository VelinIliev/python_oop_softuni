from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    mercedes_team = None
    red_bull_team = None

    def __init__(self):
        pass

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f'{team_name} has joined the new F1 season.'
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return f'{team_name} has joined the new F1 season.'
        else:
            raise ValueError('Invalid team name!')

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.mercedes_team is None or self.red_bull_team is None:
            raise Exception('Not all teams have registered for the season.')
        else:
            return_sting = ""
            return_sting += f'Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. '
            return_sting += f'Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. '
            winner = ''
            if red_bull_pos < mercedes_pos:
                winner = "Red Bull"
            else:
                winner = "Mercedes"
            return_sting += f'{winner} is ahead at the {race_name} race.'
            return return_sting
