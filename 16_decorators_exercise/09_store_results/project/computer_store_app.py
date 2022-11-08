from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Desktop Computer":
            new_computer = DesktopComputer(manufacturer, model)
            self.warehouse.append(new_computer)
            return new_computer.configure_computer(processor, ram)
        elif type_computer == "Laptop":
            new_computer = Laptop(manufacturer, model)
            self.warehouse.append(new_computer)
            return new_computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor \
                    and computer.ram >= wanted_ram:
                self.profits += (client_budget - computer.price)
                self.warehouse.remove(computer)
                return f'{computer} sold for {int(client_budget)}$.'
        raise Exception(f"Sorry, we don't have a computer for you.")

