from datetime import datetime


def now_datetime_str():
    date = datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")
