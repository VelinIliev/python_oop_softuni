from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):

        needed_memory = sum(x.memory_consumption for x in self.software_components) + software.memory_consumption
        needed_capacity = sum(x.capacity_consumption for x in self.software_components) + software.capacity_consumption

        if needed_capacity > self.capacity or needed_memory > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)
