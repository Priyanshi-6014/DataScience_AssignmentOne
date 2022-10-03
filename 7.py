def sec_to_hours_minute(seconds_pastFrom_day):  # here input is number of second past from a day
 if seconds_pastFrom_day>86400:

    seconds_pastFrom_day %= (24 * 3600)
    hours = seconds_pastFrom_day // 3600   # converting seconds to hour

    seconds_pastFrom_day %= 3600
    minutes = seconds_pastFrom_day // 60  # converting seconds to minutes

    seconds = seconds_pastFrom_day
    if hours>12:
       day = "PM"
    else:
       day = "AM"


    print(f'It is formatted as hours: minutes: seconds \n{hours}: {minutes}: {seconds} {day} ')






