# from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type):
        return next(filter(lambda d: d.__class__.__name__ == decoration_type, self.decorations), "None")


# p = Plant()
# d = DecorationRepository()
# d.add(p)
# d.add(p)
# d.remove(p)
# print(d.find_by_type("Plant"))
# d.remove(p)
# print(d.find_by_type("Plant"))
