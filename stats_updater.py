from stats_analyzer import Runescape
import time, datetime

# This is used to update everyones stats once every 4 hours
names = ['Levonski']
accts = [None] * len(names)
for i,name in enumerate(names):
    accts[i] = Runescape(name)
    
while True:
    for acct in accts:
        acct.update_stats()
    
    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print 'Stats have been updated at: ' + current_time
    time.sleep(3600*4) # 4 hours
