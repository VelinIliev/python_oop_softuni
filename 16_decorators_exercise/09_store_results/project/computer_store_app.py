from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

mapper = {
    "Desktop Computer": lambda manufacturer, model: DesktopComputer(manufacturer, model),
    "Laptop": lambda manufacturer, model: Laptop(manufacturer, model),
}


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in mapper:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        new_computer = mapper[type_computer](manufacturer, model)
        configuration = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next(filter(lambda c: c.price <= client_budget \
                                         and c.processor == wanted_processor \
                                         and c.ram >= wanted_ram, self.warehouse), None)

        if computer:
            self.profits += (client_budget - computer.price)
            self.warehouse.remove(computer)
            return f'{computer} sold for {int(client_budget)}$.'

        raise Exception(f"Sorry, we don't have a computer for you.")
