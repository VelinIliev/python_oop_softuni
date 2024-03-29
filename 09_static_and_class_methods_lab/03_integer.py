class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return f'value is not a float'

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i: i + 2] in roman:
                num += roman[value[i: i + 2]]
                i += 2
            else:
                num += roman[value[i]]
                i += 1
        new_integer = cls(num)
        return new_integer

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return f'wrong type'


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)
#
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))




# integer = Integer(1)
# print(integer.value) #, 1)

# integer = Integer.from_float(2.5)
# print(integer.value) # 2)
    #
# result = Integer.from_float("2.5")
# print(result) #"value is not a float")
    #
# integer = Integer.from_roman("XIX")
# print(integer.value) #, 19)
    #
# integer = Integer.from_string("10")
# print(integer.value) #10)
    #
result = Integer.from_string(1.5)
print(result) #, "wrong type")
