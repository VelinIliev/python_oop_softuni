from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):

        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)

        if not hardware:
            return f'Hardware does not exist'

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):

        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)

        if not hardware:
            return f'Hardware does not exist'

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)
        software = next(filter(lambda x: x.name == software_name, System._software), None)

        if not hardware or not software:
            return 'Some of the components do not exist'

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():

        total_memory_consumption_software = sum(x.memory_consumption for x in System._software)
        total_memory_consumption_hardware = sum(x.memory for x in System._hardware)
        total_capacity_consumption_soft = sum(x.capacity_consumption for x in System._software)
        total_capacity_consumption_hard = sum(x.capacity for x in System._hardware)

        output = [
            "System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
            f'Total Operational Memory: {total_memory_consumption_software} / {total_memory_consumption_hardware}',
            f"Total Capacity Taken: {total_capacity_consumption_soft} / {total_capacity_consumption_hard}"
        ]

        return "\n".join(output)

    @staticmethod
    def system_split():

        output = []

        for hardware in System._hardware:

            express_software = list(filter(lambda x: x.software_type == "Express", hardware.software_components))
            light_software = list(filter(lambda x: x.software_type == "Light", hardware.software_components))

            total_memory_used = sum(x.memory_consumption for x in hardware.software_components)
            total_capacity_used = sum(x.capacity_consumption for x in hardware.software_components)

            output.append(f'Hardware Component - {hardware.name}')
            output.append(f"Express Software Components: {len(express_software)}")
            output.append(f"Light Software Components: {len(light_software)}")
            output.append(f'Memory Usage: {total_memory_used} / {hardware.memory}')
            output.append(f'Capacity Usage: {total_capacity_used} / {hardware.capacity}')
            output.append(f'Type: {hardware.hardware_type}')
            output.append(
                f"Software Components: {', '.join(x.name for x in hardware.software_components) if hardware.software_components else 'None'}")

        return "\n".join(output)
