import time
def formatTime(seconds):
    SecinDay = 24*60*60
    if seconds>=SecinDay:
        return "More seconds than what's in a day"
    else:
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

print(formatTime(86399))