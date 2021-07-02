class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minute, seconds):
        self.hours = hours
        self.minutes = minute
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        # if self.seconds <= Time.max_seconds:
        #     return self.get_time()
        # self.seconds = 0
        # self.minutes += 1
        # if self.minutes <= Time.max_minutes:
        #     return self.get_time()
        # self.minutes = 0
        # self.hours += 1
        # if self.hours <= Time.max_hours:
        #     return self.get_time()
        # self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time.set_time(0, 0, 59)
print(time.next_second())
time2 = Time(23, 59, 59)
print(time2.next_second())
