from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage=450):
        super().__init__(brand, model, license_plate_number, max_mileage)

    def drive(self, mileage: float):
        percentage = int(round(((mileage / self.max_mileage) * 100), 0))
        self.battery_level -= percentage
