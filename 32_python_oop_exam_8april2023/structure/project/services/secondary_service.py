from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        output = [f'{self.name} Secondary Service:']
        if self.robots:
            output.append(f'Robots: {" ".join(x.name for x in self.robots)}')
        else:
            output.append(f'Robots: none')
        return "\n".join(output)
