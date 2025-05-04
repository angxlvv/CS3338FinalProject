import Reminder 
import datetime
import schedule
import time
listofschedules = []
def create_schedule(mylist):
    print("Enter time interval:")
    temptime = int(input())
    print("Enter Contents:")
    tempcontent = input()
    temp = Reminder.Reminder(temptime,tempcontent)
    mylist.append(temp)

def remind(test):
    print(test.getcontents())
def driver(templist):
    myremind = templist[0]
    
    schedule.every(2).seconds.do(remind,myremind)
    while True:
        schedule.run_pending()
        time.sleep(1)
    return
'''
remind(test1)
schedule.every(2).seconds.do(remind,test1)
while True:
    schedule.run_pending()
    time.sleep(1)
'''

create_schedule(listofschedules)
driver(listofschedules)

