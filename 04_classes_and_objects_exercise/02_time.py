class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        hours = hours
        minutes = minutes
        seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        hours = hours
        minutes = minutes
        seconds = seconds

    def get_time(self):
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    def next_second(self):
        seconds += 1
        if seconds > max_seconds:
            seconds = 0
            minutes += 1
        if minutes > max_minutes:
            minutes = 0
            hours +=1
        if hours > max_hours:
            hours = 0
        return get_time()


# time = Time(9, 30, 59)
# print(time.next_second())

# time = Time(10, 59, 59)
# print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

