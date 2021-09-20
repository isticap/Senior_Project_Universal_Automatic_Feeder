import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=17, minute='28,29')
def feed():
    subprocess.run("python3 stepper.py", shell=True)



def feed_schedule(a, b, c):
    if a == 0:
        print("no schedule set")
    elif a==1:
        print("one scheduled feeding time")
        sched.add_job(feed, 'cron', hour=b, minute=c)
        


sched.start()
# sched.print_jobs()
