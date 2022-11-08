from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profit = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            new_computer = DesktopComputer(manufacturer, model)
            result = new_computer.configure_computer(processor, ram)
        elif type_computer == "Laptop":
            new_computer = Laptop(manufacturer, model)
            result = new_computer.configure_computer(processor, ram)
        else:
            raise ValueError(f'{type_computer} is not a valid type computer!')
        self.warehouse.append(new_computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for i, computer in enumerate(self.warehouse):
            if computer.price <= client_budget and wanted_processor == computer.processor \
                    and wanted_ram <= computer.ram:
                self.profit += client_budget - computer.price
                self.warehouse.pop(i)
                return f'{computer} sold for {client_budget}$.'
        raise Exception(f"Sorry, we don't have a computer for you.")

