import time

def set_time(hours,minutes,seconds):
    hours_converted = hours * 3600
    minutes_converted = minutes * 60
    count = 0
    count = count + hours_converted
    count = count + minutes_converted
    count = count + seconds
    print(f"{count} seconds")
    for x in range(count,0,-1):
        secs = x%60
        mins = int(x/60)%60
        hrs = int(x/3600)
        print(f"{hrs}:{mins}:{secs}")
        time.sleep(1)
    print("TIMES UP")

set_time(0,0,72)
