# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from ZillowProject import send_new_house

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(send_new_house, "interval", seconds=60*60*8)

scheduler.start()
