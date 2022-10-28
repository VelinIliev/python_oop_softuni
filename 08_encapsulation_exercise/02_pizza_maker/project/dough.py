class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        # if flour_type == "":
        #     raise ValueError("The flour type cannot be an empty string")
        # if baking_technique == "":
        #     raise ValueError("The baking technique cannot be an empty string")
        # if weight <= 0:
        #     raise ValueError("The weight cannot be less or equal to zero")
        flour_type = flour_type
        baking_technique = baking_technique
        weight = weight

    @property
    def flour_type(self):
        return __flour_type

    @flour_type.setter
    def flour_type(self, value):
        if not value:
            raise ValueError("The flour type cannot be an empty string")
        __flour_type = value

    @property
    def baking_technique(self):
        return __baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if not value:
            raise ValueError("The baking technique cannot be an empty string")
        __baking_technique = value

    @property
    def weight(self):
        return __weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        __weight = value
