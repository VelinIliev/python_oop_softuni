from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        return None

    # @property
    # def budget(self):
    #     return self._budget
    #
    # @budget.setter
    # def budget(self, value):
    #     if value < 1000000:
    #         raise ValueError("F1 is an expensive sport, find more sponsors!")
    #     self._budget = value

