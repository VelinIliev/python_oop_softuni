class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app:str, memory:int):
        if self.memory - memory >= 0 and self.is_on:
            self.memory -= memory
            self.apps.append(app)
            return f'Installing {app}'
        elif self.memory - memory >= 0 and not self.is_on:
            return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
