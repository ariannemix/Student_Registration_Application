import time


def get_time():
    seconds = time.time()
    day = time.ctime(seconds)
    day = day.split()
    yyyy = day[4]
    months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
              'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    mm = months[day[1]]
    dd = day[2]
    hour = day[3]
    actual = yyyy, mm, dd, hour
    return ' '.join(actual)
