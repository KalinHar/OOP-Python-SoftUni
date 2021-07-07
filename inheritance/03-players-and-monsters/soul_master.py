from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return super().__str__()
