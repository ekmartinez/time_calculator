
def add_time(start, duration, day=None):
    #Parses input string.
    hour = int(start.split(" ")[0].split(":")[0])
    minute = int(start.split(" ")[0].split(":")[1])
    startMeridiem = start.split(" ")[1]
    durationHours = int(duration.split(" ")[0].split(":")[0])
    durationMinutes = int(duration.split(" ")[0].split(":")[1]) 

    #Converts meridiem into boolean for further processing.
    if startMeridiem == 'AM':
        meridiem = True
    elif startMeridiem == 'PM':
        meridiem = False

    weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    dayCounter = 0
    if day == None:
        currentDay = 0
    else:
        currentDay = weekDays.index(day.capitalize())
    
    while durationMinutes > 0:
        durationMinutes -= 1
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 12:
                if meridiem == False: 
                    currentDay += 1
                    dayCounter += 1
                    if currentDay == 7:
                        currentDay = 0 
                meridiem = not meridiem 
            if hour == 13:
                hour = 1
    #To keep leading zero.
    if minute < 10:
        minute = '%02d' % minute
    else:
        minute = str(minute)
    
    while durationHours > 0:
        durationHours -= 1
        hour += 1
        if hour == 12:
            if meridiem == False:
                currentDay += 1
                dayCounter += 1
                if currentDay == 7:
                    currentDay = 0 
            meridiem = not meridiem
        if hour == 13:
            hour = 1 

    meridiem = 'AM' if meridiem == True else "PM" 

    #Returns results based on optional parameter.
    if day == None:
        if dayCounter == 0:
            return f'{hour}:{minute} {meridiem}'    
        elif dayCounter == 1:
            return f'{hour}:{minute} {meridiem} (next day)'
        elif dayCounter > 1:
            return f'{hour}:{minute} {meridiem} ({dayCounter} days later)'         
    else:
        if dayCounter == 0: 
            return f'{hour}:{minute} {meridiem}, {weekDays[weekDays.index(day.capitalize())]}'
        elif dayCounter == 1:
            return f'{hour}:{minute} {meridiem}, {weekDays[currentDay]} (next day)'
        elif dayCounter > 1:
            return f'{hour}:{minute} {meridiem}, {weekDays[currentDay]} ({dayCounter} days later)'
    
print(add_time("11:59 PM", "24:05"))

