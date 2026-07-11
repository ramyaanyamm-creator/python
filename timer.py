import time
my_time=20
for i in range(my_time,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    print(f"00-{minutes:02}-{seconds:02}")
    time.sleep(5)
