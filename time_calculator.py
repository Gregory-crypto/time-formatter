def add_time(start, duration, day = ''):

    s_hours = int(start.split(' ')[0].split(':')[0])
    s_minutes = int(start.split(' ')[0].split(':')[1])

    if start.split(' ')[1] == 'PM':
        s_hours += 12
    
    
    d_hours = int(duration.split(':')[0])
    d_minutes = int(duration.split(':')[1])

    end_minutes = (s_minutes + d_minutes) % 60
    pre_end_hours = s_hours + d_hours + ((s_minutes + d_minutes) // 60) 

    if end_minutes < 10:
        end_minutes = '0' + str(end_minutes)
    else:
        end_minutes = str(end_minutes)
    # if you have more than 60 minutes, the number of hours will be increased

    counter = pre_end_hours // 24
    if counter == 1:
        counter = 1
        ext_day = ' (next day)'
    elif counter > 1:
        ext_day = f' ({pre_end_hours // 24} days later)'
    else:
        ext_day = ''

    pre_end_hours %= 24

    if pre_end_hours == 0:
        end_hours = str((pre_end_hours + 12)) + ':' + end_minutes + ' AM'
    elif pre_end_hours < 12:
        end_hours = str((pre_end_hours)) + ':' + end_minutes + ' AM'
    elif pre_end_hours == 12:
        end_hours = str((pre_end_hours)) + ':' + end_minutes + ' PM'
    else:
        end_hours = str((pre_end_hours) - 12) + ':' + end_minutes + ' PM'
    

    if day != '':
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = (week.index(day.lower().capitalize()) + counter) % 7
        day = week[day_index]
        end_hours += (', ' + day)

    return end_hours + ext_day
