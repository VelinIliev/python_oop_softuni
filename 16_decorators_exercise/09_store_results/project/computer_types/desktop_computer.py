from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    # processors = {
    #     "AMD Ryzen 7 5700G": 500,
    #     "Intel Core i5-12600K": 600,
    #     "Apple M1 Max": 1800
    # }
    # rams = [2, 4, 8, 16, 32, 64, 128]
    # computer_type = 'desktop computer'

    @property
    def processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def rams(self):
        return [2, 4, 8, 16, 32, 64, 128]

    @property
    def computer_type(self):
        return 'desktop computer'
