import time

def date_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

time = date_time()

print(f"Current Time: {time}")