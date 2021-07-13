class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room_take = room.take_room(people)
                if not room_take:
                    self.guests += room.guests

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"

