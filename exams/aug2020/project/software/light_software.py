from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", capacity_consumption * 1.5, memory_consumption / 2)


# light = LightSoftware("Namem", 4, 6)
# print(light.__dict__)