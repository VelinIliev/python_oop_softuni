class Topping:
    def __init__(self, topping_type: str, weight: float):
        if topping_type == "":
            raise ValueError("The topping type cannot be an empty string")
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        topping_type = topping_type
        weight = weight

    @property
    def topping_type(self):
        return __topping_type

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        __topping_type = value

    @property
    def weight(self):
        return __weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        __weight = value
