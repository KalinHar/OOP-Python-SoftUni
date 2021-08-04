class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_capacity = 0
        self.used_memory = 0

    def install(self, software):
        if software.capacity_consumption <= self.capacity - self.used_capacity\
                and software.memory_consumption <= self.memory - self.used_memory:
            self.software_components.append(software)
            self.used_capacity += software.capacity_consumption
            self.used_memory += software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        self.software_components.remove(software)
        self.used_capacity -= software.capacity_consumption
        self.used_memory -= software.memory_consumptio