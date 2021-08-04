from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        p_hard = PowerHardware(name, capacity, memory)
        System._hardware.append(p_hard)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        h_hard = HeavyHardware(name, capacity, memory)
        System._hardware.append(h_hard)

    @staticmethod
    def get_obj(objects, name):
        return next(filter(lambda x: x.name == name, objects), None)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = System.get_obj(System._hardware, hardware_name)
        if not hard:
            return "Hardware does not exist"
        e_soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(e_soft)
            System._software.append(e_soft)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = System.get_obj(System._hardware, hardware_name)
        if not hard:
            return "Hardware does not exist"
        l_soft = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(l_soft)
            System._software.append(l_soft)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hard = System.get_obj(System._hardware, hardware_name)
            soft = System.get_obj(hard.software_components, software_name)
            hard.uninstall(soft)
            System._software.remove(soft)
        except:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ["System Analysis"]
        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {int(sum(h.used_memory for h in System._hardware))}"
                      f" / {int(sum(h.memory for h in System._hardware))}")
        result.append(f"Total Capacity Taken: {int(sum(h.used_capacity for h in System._hardware))}"
                      f" / {int(sum(h.capacity for h in System._hardware))}")
        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"\
                      f"Express Software Components: {len(list(comp for comp in h.software_components if isinstance(comp, ExpressSoftware)))}\n"\
                      f"Light Software Components: {len(list(comp for comp in h.software_components if isinstance(comp, LightSoftware)))}\n"\
                      f"Memory Usage: {int(h.used_memory)} / {int(h.memory)}\n"\
                      f"Capacity Usage: {int(h.used_capacity)} / {int(h.capacity)}\n"\
                      f"Type: {h.type}\n"
            names = list(comp.name for comp in h.software_components)
            if not names:
                names = None
            result += f"Software Components: {', '.join(names)}"
        return result


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
