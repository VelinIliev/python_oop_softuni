from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar

vehicles_mapper = {
    "CargoVan": CargoVan,
    "PassengerCar": PassengerCar
}


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users), None)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in vehicles_mapper:
            return f'Vehicle type {vehicle_type} is inaccessible.'

        vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles), None)

        if vehicle:
            return f'{license_plate_number} belongs to another vehicle.'

        vehicle = vehicles_mapper[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route = next(filter(lambda x: x.start_point == start_point and x.end_point == end_point and x.length == length,
                            self.routes), None)

        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        route = next(filter(lambda x: x.start_point == start_point and x.end_point == end_point and x.length < length,
                            self.routes), None)

        if route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        longer_route = next(
            filter(lambda x: x.start_point == start_point and x.end_point == end_point and x.length > length,
                   self.routes), None)

        if longer_route:
            longer_route.is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):

        user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users), None)
        vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles), None)
        route = next(filter(lambda x: x.route_id == route_id, self.routes), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):

        vehicles = list(filter(lambda x: x.is_damaged, self.vehicles))
        vehicles = sorted(vehicles, key=lambda x: (x.brand, x.model))
        vehicles = vehicles[:count:]

        for vehicle in vehicles:
            vehicle.recharge()
            vehicle.change_status()

        return f"{len(vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        output = ["*** E-Drive-Rent ***"]

        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        for user in sorted_users:
            output.append(str(user))

        return "\n".join(output)
