from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

service_mapper = {
    "MainService": MainService,
    "SecondaryService": SecondaryService
}

robots_mapper = {
    "FemaleRobot": FemaleRobot,
    "MaleRobot": MaleRobot
}


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in service_mapper:
            raise Exception("Invalid service type!")

        service = service_mapper[service_type](name)
        self.services.append(service)
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in robots_mapper:
            raise Exception("Invalid robot type!")

        robot = robots_mapper[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda x: x.name == robot_name, self.robots), None)
        service = next(filter(lambda x: x.name == service_name, self.services), None)

        if (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService") or \
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService"):
            return f'Unsuitable service.'

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        robot = next(filter(lambda x: x.name == robot_name, service.robots), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        for r in service.robots:
            r.eating()
        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        total = 0
        for r in service.robots:
            total += r.price
        return f'The value of service {service_name} is {total:.2f}.'

    def __str__(self):
        output = []

        for service in self.services:
            output.append(service.details())

        return "\n".join(output)
