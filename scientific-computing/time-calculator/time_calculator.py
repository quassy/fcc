# import re


def add_time(
    start: str,
    duration: str,
    weekday: str = "",
):
#    pattern = "^(\d*):(\d*)[\s]?(AM|PM)?$"
#    now = re.match(pattern, start)
#    plus = re.match(pattern, duration)

#    now_h = int(now.group(1))
#    now_m = int(now.group(2))
#    now_n = 12 if now.group(3) == "PM" else 0

#    plus_h = int(plus.group(1))
#    plus_m = int(plus.group(2))

    now_h = int(start[:-6])
    now_m = int(start[-5:-3])
    now_n = 12 if start[-2:] == "PM" else 0

    plus_h = int(duration[:-3])
    plus_m = int(duration[-2:])

    then = (now_n + now_h + plus_h) * 60 + now_m + plus_m

    days = then // (24 * 60)
    if days == 0:
        days_str = ""
    elif days == 1:
        days_str = " (next day)"
    elif days >= 2:
        days_str = f" ({days} days later)"
    if weekday != "":
        weekday = weekday[:1].upper() + weekday[1:].lower()
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        weekday_str = ", " + weekdays[(weekdays.index(weekday) + days) % 7]
    else:
        weekday_str = ""
    
    hours = then % (24 * 60) // 60
    if hours < 12:
        noon_str = " AM"
    elif hours >= 12:
        noon_str = " PM"
        hours -= 12
    if hours == 0:
        hours = 12

    mins = then % (24 * 60) % 60

    return f"{hours}:{mins:02d}{noon_str}{weekday_str}{days_str}"