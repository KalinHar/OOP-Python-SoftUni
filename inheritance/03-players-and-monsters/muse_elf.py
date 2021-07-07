from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return super().__str__()
