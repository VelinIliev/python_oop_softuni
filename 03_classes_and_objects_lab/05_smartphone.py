class Smartphone:
    def __init__(self, memory: int):
        memory = memory
        apps = []
        is_on = False

    def power(self):
        if is_on:
            is_on = False
        else:
            is_on = True

    def install(self, app:str, memory:int):
        if memory - memory >= 0 and is_on:
            memory -= memory
            apps.append(app)
            return f'Installing {app}'
        elif memory - memory >= 0 and not is_on:
            return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(apps)}. Memory left: {memory}'

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
