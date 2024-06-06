class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def isEqual(self, other):
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

def get_time_from_user(prompt):
    hour = int(input(f"{prompt} - hour: "))
    minute = int(input(f"{prompt} - minute: "))
    second = int(input(f"{prompt} - second: "))
    return Time(hour, minute, second)

print("Please enter the first time: ")
time1 = get_time_from_user("first time")
print("Please enter the second time: ")
time2 = get_time_from_user("second time")

if time1.isEqual(time2):
    print("Times are equal")
else:
    print("Times aren't equal")